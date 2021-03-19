import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import {
  WebAnalysisFullDetails,
  WebAnalysisListDetails,
  WordCounts
} from 'src/app/webAnalysisDetails.model'
import { WebanalysislistService } from 'src/app/webanalysislist.service';
import { UrlsService } from 'src/app/urls.service';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-queryhistory',
  templateUrl: './queryhistory.component.html',
  styleUrls: ['./queryhistory.component.css']
})
export class QueryhistoryComponent implements OnInit {

  @ViewChild("sortDescCheckboxElem", {static:false}) sortDescCheckboxElem:ElementRef;

  constructor(
    private _webAnalysisService:WebanalysislistService,
    private _url:UrlsService,
    private _api:ApiService
  ) { }

  ngOnInit() {

  }

  ngAfterViewInit() {
    this.sortDescCheckboxElem.nativeElement.checked = this.pageSearchParamSortIsDesc()
  }

  webAnalysisList():WebAnalysisListDetails[] {
    return this._webAnalysisService.webAnalysisList
  }

  pageSearchParamSortIsDesc():boolean {
    const pageQueryParams = this._url.getParsedPageQueryParams()
    const validSortValues = this._webAnalysisService.validSortValues
    const defaultValue = true
    for (let qsKey of Object.keys(pageQueryParams)) {
      if(qsKey == 'sort' && validSortValues.indexOf(pageQueryParams[qsKey]) != -1) {
        return /^-/.test(pageQueryParams[qsKey]) // Is DESC if value starts with "-"
      }
    }
    return defaultValue
  }

  sortByCreatedAt() {
    const pageOrigin = window.location.origin
    const isDesc = this.sortDescCheckboxElem.nativeElement.checked
    window.location.href = `${pageOrigin}?sort=${isDesc ? '-' : ''}created_at`
  }

  sortByCharCount() {
    const pageOrigin = window.location.origin
    const isDesc = this.sortDescCheckboxElem.nativeElement.checked
    window.location.href = `${pageOrigin}?sort=${isDesc ? '-' : ''}page_content_length`
  }

  async clearHistoryBtnClick() {
    if (!confirm("Are you sure you want to delete your history of web queries?")) {
      return
    }
    const response = await this._api.delete(this._url.deleteWebAnaylsisListUrl)
    // FIXME: response here is null. Check the status code == 204
    this._webAnalysisService.clearWebAnalysisList()

  }

}
