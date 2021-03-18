import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  STATUS_200_OK = 200
  STATUS_201_CREATED = 201
  STATUS_204_NO_CONTENT = 204
  STATUS_502_BAD_GATEWAY = 502

  constructor(
    private _http: HttpClient
  ) { }

  get(url:string):Promise<any> {
    return this._http.get(url).toPromise();
  }

  post(url:string, data:any):Promise<any> {
    return this._http.post(url, data).toPromise();
  }

  delete(url:string):Promise<any> {
    return this._http.delete(url).toPromise();
  }

}
