import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HeadingbarComponent } from './headingbar.component';

describe('HeadingbarComponent', () => {
  let component: HeadingbarComponent;
  let fixture: ComponentFixture<HeadingbarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HeadingbarComponent ]
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
