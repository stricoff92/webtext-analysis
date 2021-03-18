import { Component, OnInit } from '@angular/core';

import { UrlsService } from 'src/app/urls.service'
import { UserService } from '../user.service';
import { UserDetails } from 'src/app/userdetails.model'

@Component({
  selector: 'app-headingbar',
  templateUrl: './headingbar.component.html',
  styleUrls: ['./headingbar.component.css']
})
export class HeadingbarComponent implements OnInit {

  logoutUrl:string
  loggedInUsername:string

  constructor(
    private _url:UrlsService,
    private _user:UserService
  ) {
    this.logoutUrl = this._url.logoutUrl
    this.setLoggedInUsername()
  }

  ngOnInit() {

  }

  async setLoggedInUsername() {
    const userDetails:UserDetails = await this._user.getUserDetails()
    this.loggedInUsername = userDetails.username
  }

}
