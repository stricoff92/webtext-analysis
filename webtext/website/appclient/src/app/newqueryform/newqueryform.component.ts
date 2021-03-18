import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { UrlsService } from '../urls.service';
import { NewAnalysisRequestData } from 'src/app/newAnalysisRequestData.model';
import { ApiService } from '../api.service';
import { WebAnalysisFullDetails } from 'src/app/webAnalysisDetails.model'

@Component({
  selector: 'app-newqueryform',
  templateUrl: './newqueryform.component.html',
  styleUrls: ['./newqueryform.component.css']
})
export class NewqueryformComponent implements OnInit {

  @ViewChild("runQueryBtnElem", {static: false}) runQueryBtnElem:ElementRef;
  @ViewChild("targetUrlInputElem", {static: false}) targetUrlInputElem:ElementRef;

  errorMessage:string = ""
  runQueryButtonEnabled:boolean = true
  showLoadingSpinner:boolean = false

  targetUrlInput:string = "https://";
  scrapeModeInput:string = "static";

  constructor(
    private _url:UrlsService,
    private _api:ApiService
  ) { }

  ngOnInit() {
  }

  closeErrorAlert() {
    this.errorMessage = ""
  }

  disableRunQueryBtn() {
    this.runQueryButtonEnabled = false
    this.runQueryBtnElem.nativeElement.classList.add("disabled")
  }

  enableRunQueryBtn() {
    this.runQueryButtonEnabled = true
    this.runQueryBtnElem.nativeElement.classList.remove("disabled")
  }

  async runQueryBtnClick() {
    if(!this.runQueryButtonEnabled) {
      return
    }

    const url = this.targetUrlInput
    const scrapeMode = this.scrapeModeInput

    this.disableRunQueryBtn()

    if(!this._url.urlIsValid(url)) {
      this.enableRunQueryBtn()
      this.errorMessage = "URL is not valid."
      return
    }

    this.showLoadingSpinner = true

    const data:NewAnalysisRequestData = {
      target_url:url,
      analysis_mode:scrapeMode,
    }

    let webAnalysis:WebAnalysisFullDetails;
    try {
      webAnalysis = await this._api.post(this._url.createWebAnalysisUrl, data)
    } catch(err) {
      // Query Failed
      if(err.status == this._api.STATUS_502_BAD_GATEWAY && (err.error || {}).error) {
        this.errorMessage = err.error.error
      } else {
        this.errorMessage = `An error occured, code:${err.status}`
      }
      this.showLoadingSpinner = false
      this.enableRunQueryBtn()
      return
    }

    // Query successful
    this.showLoadingSpinner = false
    this.enableRunQueryBtn()
    console.log(webAnalysis)

  }

}
