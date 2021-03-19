import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { QueryhistoryrowComponent } from './queryhistoryrow.component';

describe('QueryhistoryrowComponent', () => {
  let component: QueryhistoryrowComponent;
  let fixture: ComponentFixture<QueryhistoryrowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QueryhistoryrowComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QueryhistoryrowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
