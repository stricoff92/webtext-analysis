import { TestBed } from '@angular/core/testing';

import { WebanalysislistService } from './webanalysislist.service';

describe('WebanalysislistService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WebanalysislistService = TestBed.get(WebanalysislistService);
    expect(service).toBeTruthy();
  });
});
