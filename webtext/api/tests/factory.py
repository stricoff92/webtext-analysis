
from api.lib.content_types import (
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_HTML,
)
from api.models import WebAnalysis


class TestObjectFactory:

    def create_web_analysis(
        self, owner, page_content:str, page_content_length:int, target_url:str,
        analysis_mode=WebAnalysis.ANALYSIS_MODE_STATIC,
        page_content_type=CONTENT_TYPE_TEXT):

        return WebAnalysis.objects.create(
            owner=owner, target_url=target_url,page_content=page_content,
            page_content_length=page_content_length, analysis_mode=analysis_mode,
            page_content_type=page_content_type)


class MockHTTPResponse:
    def __init__(self, status_code:int, content:bytes, headers={}, exception_to_raise=None):
        self.status_code = status_code
        self.content = content
        self.headers = headers
        self.exception_to_raise = exception_to_raise

    def raise_for_status(self):
        if self.exception_to_raise:
            raise exception_to_raise
