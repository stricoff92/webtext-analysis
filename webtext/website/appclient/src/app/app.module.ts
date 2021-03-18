import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeadingbarComponent } from './headingbar/headingbar.component';
import { NewqueryformComponent } from './newqueryform/newqueryform.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadingbarComponent,
    NewqueryformComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken', // TODO: Verify if this needs to be updated
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
