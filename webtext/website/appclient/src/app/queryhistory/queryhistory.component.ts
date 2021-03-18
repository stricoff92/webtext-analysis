import { Component, OnInit } from '@angular/core';
import { WebanalysislistService } from 'src/app/webanalysislist.service'
import {
  WebAnalysisFullDetails,
  WebAnalysisListDetails,
  WordCounts
} from 'src/app/webAnalysisDetails.model'

@Component({
  selector: 'app-queryhistory',
  templateUrl: './queryhistory.component.html',
  styleUrls: ['./queryhistory.component.css']
})
export class QueryhistoryComponent implements OnInit {



  constructor(
    private _webAnalysisService:WebanalysislistService
  ) { }

  ngOnInit() {
  }

  webAnalysisList():WebAnalysisListDetails[] {
    return this._webAnalysisService.webAnalysisList
  }

}
