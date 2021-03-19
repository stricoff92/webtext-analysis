import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { QueryhistoryComponent } from './queryhistory.component';
import { QueryhistoryrowComponent } from '../queryhistoryrow/queryhistoryrow.component'


describe('QueryhistoryComponent', () => {
  let component: QueryhistoryComponent;
  let fixture: ComponentFixture<QueryhistoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QueryhistoryComponent, QueryhistoryrowComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QueryhistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
