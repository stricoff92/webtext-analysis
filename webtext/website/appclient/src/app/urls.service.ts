import { Injectable } from '@angular/core';

import * as urljoin from 'url-join';

@Injectable({
  providedIn: 'root'
})
export class UrlsService {

  logoutUrl = "/logout/"

  baseAPIUrl = "/api/v1/"
  getUserInfoUrl:string
  getWebAnaylsisListUrl:string
  createWebAnalysisUrl:string

  constructor() {
    this.getUserInfoUrl = this.join(this.baseAPIUrl, 'user', 'details')
    this.createWebAnalysisUrl = this.join(this.baseAPIUrl, 'web-analysis', 'create')
    this.getWebAnaylsisListUrl = this.join(this.baseAPIUrl, 'web-analysis', 'list')
  }

  getWebAnalysisDetailsUrl(slug:string):string {
    return this.join(this.baseAPIUrl, "web-analysis", slug, "details")
  }


  join(...parts):string {
    let urlStr:string = urljoin(...parts).trim()
    if(!this.urlEndsWithSlash(urlStr) && !this.urlContainsQueryParams(urlStr)) {
      urlStr = urlStr + "/"
    }
    return urlStr
  }

  urlIsValid(url:string):boolean {
    if(!/^https?:\/\//.test(url)) {
      return false // We expect urls to start with "http://"
    }
    return /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/.test(url)
  }

  private urlEndsWithSlash(url:string):boolean {
    return /\/$/.test(url)
  }

  private urlContainsQueryParams(url:string):boolean {
    const urlLength:number = url.length
    const countOfQuestionmarks:number = url.split('?').length - 1
    if(countOfQuestionmarks === 0) {
      return false
    } else if(countOfQuestionmarks === 1) {
      return (urlLength - 1) != url.indexOf("?") // Verify "?" is not the last character
    } else {
      throw new Error(`url ${url} contains unexpected number of char \"?\"`)
    }
  }

}
