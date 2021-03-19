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

  it('should check the DESC sort checkbox by default', ()=>{
    expect(component.sortDescCheckboxElem.nativeElement.checked).toBeTruthy()
  })

  it('should not check the DESC sort checkbox if url params contain an ASC sort param', ()=>{
    // TODO: Write this
  })

  it('should check the DESC sort checkbox if url params contain an DESC sort param', ()=>{
    // TODO: Write this
  })

});
