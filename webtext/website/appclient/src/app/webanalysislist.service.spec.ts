import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { WebanalysislistService } from './webanalysislist.service';

describe('WebanalysislistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [WebanalysislistService]
    })
  });

  it('should be created', () => {
    const service: WebanalysislistService = TestBed.get(WebanalysislistService);
    expect(service).toBeTruthy();
  });
});
