import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import * as moment from 'moment';

import {
  WebAnalysisListDetails,
  WebAnalysisFullDetails
} from 'src/app/webAnalysisDetails.model'
import { ApiService } from '../api.service';
import { UrlsService } from '../urls.service';


@Component({
  selector: 'app-queryhistoryrow',
  templateUrl: './queryhistoryrow.component.html',
  styleUrls: ['./queryhistoryrow.component.css']
})
export class QueryhistoryrowComponent implements OnInit {

  @ViewChild("rowCardHeader", {static:false}) rowCardHeader:ElementRef
  @Input() webAnalysisData:WebAnalysisListDetails

  rowExpanded = false
  sortedWordCounts:{value:string, count:number}[] = []

  constructor(
    private _url:UrlsService,
    private _api:ApiService
  ) {
  }

  ngOnInit() {
    this.rowExpanded = !!this.webAnalysisData.page_content
    if(this.rowExpanded) {
      this.buildSortedWordCountArray()
    }
  }

  page_content_length_with_commas():string {
    return this.numberWithCommas(this.webAnalysisData.page_content_length)
  }

  created_at_formatted():string {
    // Convert TZ aware UTC timestamp to localized human readable datetime.
    const created_at:moment.Moment = moment(this.webAnalysisData.created_at);
    return created_at.format("lll") // example formatted string: "Mar 18, 2021 9:07 PM"
  }

  // TODO: move this function to another file?
  numberWithCommas(x:number):string {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

  expandRow():void {
    if(this.rowExpanded) {
      return
    }
    this.rowExpanded = true
    this.rowCardHeader.nativeElement.classList.remove("clickable-item")
    this.fetchFullRowDetails()
  }

  private async fetchFullRowDetails():Promise<void> {
    const apiUrl = this._url.getWebAnalysisDetailsUrl(this.webAnalysisData.slug)
    const webAnalysis:WebAnalysisFullDetails = await this._api.get(apiUrl)

    this.webAnalysisData = webAnalysis
    this.buildSortedWordCountArray()
  }

  private buildSortedWordCountArray():void {
    const words:string[] = Object.keys(this.webAnalysisData.word_counts)
    for(let i in words) {
      let word = words[i]
      this.sortedWordCounts.push(
        {value:word, count:this.webAnalysisData.word_counts[word]})
    }
    this.sortedWordCounts.sort((v1, v2)=>{
      return v2.count > v1.count ? 1 : -1
    })
  }


}
