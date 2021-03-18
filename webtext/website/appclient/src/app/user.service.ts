
import { Injectable } from '@angular/core';
import { UrlsService } from 'src/app/urls.service';
import { ApiService } from './api.service';
import { UserDetails } from 'src/app/userdetails.model'


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private _url:UrlsService,
    private _api:ApiService
  ) {

  }

  async getUserDetails():Promise<UserDetails> {
    const data:UserDetails = await this._api.get(this._url.getUserInfoUrl)
    return data
  }

}
