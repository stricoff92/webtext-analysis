import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QueryhistoryrowComponent } from './queryhistoryrow.component';

describe('QueryhistoryrowComponent', () => {
  let component: QueryhistoryrowComponent;
  let fixture: ComponentFixture<QueryhistoryrowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QueryhistoryrowComponent ]
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
