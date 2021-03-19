

from django.conf import settings
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

class HeadlessModeNotConfiguredError(WebScrapeError):
    pass


def scrape_page(target_url:str, mode:str) -> tuple:
    """ Given a web url and a method for scraping,
        retrieve the resource and return it as a tuple of (page_text, content_type,).
    """
    if mode == WebAnalysis.ANALYSIS_MODE_STATIC:
        return  scrape_static_page(target_url)
    elif mode == WebAnalysis.ANALYSIS_MODE_HEADLESS:
        return scrape_with_headless_browser(target_url)


def scrape_static_page(target_url:str, timeout_seconds=5) -> tuple:
    """ Make a single GET request and download whatever text the server offers.
    """
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


def scrape_with_headless_browser(target_url:str) -> tuple:
    """ Start a headless browser session, navigate to the page, and scrape all text from the DOM.
    """
    if not settings.CHROME_SELENIUM_DRIVER_PATH:
        raise HeadlessModeNotConfiguredError("Headless browser mode is not configured.")

    (_, content_type) = scrape_static_page(target_url)

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(settings.CHROME_SELENIUM_DRIVER_PATH, chrome_options=options)

    try:
        page_text = _get_text_from_headless_session(driver, target_url)
    except Exception:
        raise
    finally:
        driver.close()

    return (
        page_text,
        content_type,
    )


def _get_text_from_headless_session(driver, target_url:str):
    # Thanks https://stackoverflow.com/questions/25356440/need-to-dump-entire-dom-tree-with-element-id-from-selenium-server
    driver.get(target_url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    return html
