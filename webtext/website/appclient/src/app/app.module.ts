import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeadingbarComponent } from './headingbar/headingbar.component';
import { NewqueryformComponent } from './newqueryform/newqueryform.component';
import { QueryhistoryComponent } from './queryhistory/queryhistory.component';
import { QueryhistoryrowComponent } from './queryhistoryrow/queryhistoryrow.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadingbarComponent,
    NewqueryformComponent,
    QueryhistoryComponent,
    QueryhistoryrowComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
