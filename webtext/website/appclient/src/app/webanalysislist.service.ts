import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { UrlsService } from './urls.service';
import {
  WebAnalysisFullDetails,
  WebAnalysisListDetails,
  WordCounts
} from 'src/app/webAnalysisDetails.model'

@Injectable({
  providedIn: 'root'
})
export class WebanalysislistService {

  webAnalysisList:WebAnalysisListDetails[] = []

  constructor(
    private _api:ApiService,
    private _url:UrlsService
  ) {
    const startPage = 1
    this.fetchWebAnalysisList(startPage)
  }

  registerNewWebAnalysis(webAnalysis:WebAnalysisFullDetails):void {
    this.webAnalysisList.unshift(webAnalysis)
  }

  private async fetchWebAnalysisList(page:number):Promise<void> {
    const apiUrl = `${this._url.getWebAnaylsisListUrl}?page=${page}`
    const response:{rows:WebAnalysisListDetails[], another_page:boolean} = await this._api.get(apiUrl)
    if (response.rows.length) {
      this.webAnalysisList = this.webAnalysisList.concat(response.rows)
    }
    if (response.another_page) {
      let nextPage = page + 1
      this.fetchWebAnalysisList(nextPage)
    }
  }

}
