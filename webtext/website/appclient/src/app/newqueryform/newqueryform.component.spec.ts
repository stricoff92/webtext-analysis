import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { FormsModule } from '@angular/forms';

import { NewqueryformComponent } from './newqueryform.component';

describe('NewqueryformComponent', () => {
  let component: NewqueryformComponent;
  let fixture: ComponentFixture<NewqueryformComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewqueryformComponent ],
      imports: [HttpClientTestingModule, FormsModule],
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
