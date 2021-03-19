import { TestBed, async } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HeadingbarComponent } from 'src/app/headingbar/headingbar.component';
import { NewqueryformComponent } from 'src/app/newqueryform/newqueryform.component';
import { QueryhistoryComponent } from 'src/app/queryhistory/queryhistory.component';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        AppComponent,
        HeadingbarComponent,
        NewqueryformComponent,
        QueryhistoryComponent
      ],
      imports:[
        FormsModule
      ]
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'appclient'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.title).toEqual('appclient');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('.content span').textContent).toContain('appclient app is running!');
  });
});
