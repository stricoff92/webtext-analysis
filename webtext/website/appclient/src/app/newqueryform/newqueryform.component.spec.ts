import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewqueryformComponent } from './newqueryform.component';

describe('NewqueryformComponent', () => {
  let component: NewqueryformComponent;
  let fixture: ComponentFixture<NewqueryformComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewqueryformComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewqueryformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
