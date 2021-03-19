import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HeadingbarComponent } from './headingbar.component';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

describe('HeadingbarComponent', () => {
  let component: HeadingbarComponent;
  let fixture: ComponentFixture<HeadingbarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HeadingbarComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HeadingbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
