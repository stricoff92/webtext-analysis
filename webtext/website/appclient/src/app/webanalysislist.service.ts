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
  searchParams:any = {}

  // TODO: dynamically generate this list from the API
  validSortValues = ['created_at', '-created_at', 'page_content_length', '-page_content_length']

  constructor(
    private _api:ApiService,
    private _url:UrlsService,
  ) {
    this.searchParams = this._url.getParsedPageQueryParams()
    const startPage = 1
    this.fetchWebAnalysisList(startPage)
  }

  registerNewWebAnalysis(webAnalysis:WebAnalysisFullDetails):void {
    this.webAnalysisList.unshift(webAnalysis)
  }

  clearWebAnalysisList():void {
    this.webAnalysisList =[]
  }

  private async fetchWebAnalysisList(page:number):Promise<void> {
    let apiUrl = `${this._url.getWebAnaylsisListUrl}?page=${page}`

    // If page url has a valid `sort=sortkey` urlquery, add it to the api url.
    for (let qsKey of Object.keys(this.searchParams)) {
      if(qsKey == 'sort' && this.validSortValues.indexOf(this.searchParams[qsKey]) != -1) {
        apiUrl = apiUrl + `&${qsKey}=${this.searchParams[qsKey]}`
        break
      }
    }

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
