

import requests

from api.models import WebAnalysis
from api.lib.content_types import (
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_HTML,
)

class WebScrapeError(Exception):
    pass

class HTTPTimeoutError(WebScrapeError):
    pass

class InvalidHTTPStatusCodeError(WebScrapeError):
    pass

class InvalidHTTPContentTypeError(WebScrapeError):
    @classmethod
    def validate_content_type(cls, response):
        valid_content_types = (CONTENT_TYPE_TEXT, CONTENT_TYPE_HTML,)
        returned_content_type = response.headers.get("content-type")
        for valid_content_type in valid_content_types:
            if valid_content_type in returned_content_type:
                return
        raise cls(f"Received invalid content type: {returned_content_type}")


def scrape_page(target_url:str, mode:str) -> tuple:
    """ Given a web url and a method for scraping,
        retrieve the resource and return it as a tuple of (page_text, content_type,).
    """
    if mode == WebAnalysis.ANALYSIS_MODE_STATIC:
        return  scrape_static_page(target_url)


def scrape_static_page(target_url:str, timeout_seconds=5) -> tuple:
    try:
        response = requests.get(target_url, timeout=timeout_seconds)
    except requests.Timeout:
        raise HTTPTimeoutError(
            f"Downstream connection timed out after {timeout_seconds} seconds.")
    except requests.RequestException as e:
        raise WebScrapeError(
            f"Could not connect to the downstream server.")

    try:
        response.raise_for_status()
    except requests.HTTPError:
        raise InvalidHTTPStatusCodeError(
            f"Received downstream HTTP status {response.status_code}.")

    InvalidHTTPContentTypeError.validate_content_type(response)

    return (
        response.content.decode(),
        response.headers['content-type'],
    )
