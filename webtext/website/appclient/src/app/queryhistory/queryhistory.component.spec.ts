import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QueryhistoryComponent } from './queryhistory.component';

describe('QueryhistoryComponent', () => {
  let component: QueryhistoryComponent;
  let fixture: ComponentFixture<QueryhistoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QueryhistoryComponent ]
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
