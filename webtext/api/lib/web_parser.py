
import re

from bs4 import BeautifulSoup
from bs4.element import Comment

from api.lib.content_types import (
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_HTML,
)


MULTI_SPACE_PATTERN = re.compile(r"\s+")
NON_VISIBLE_TAGS = set(['style', 'script', 'head', 'title', 'meta', '[document]'])


def parse_resonse_content(response_content:str, content_type:str) -> str:
    if CONTENT_TYPE_TEXT in content_type:
        return parse_reponse_content_plain_text(response_content)
    elif CONTENT_TYPE_HTML in content_type:
        return parse_reponse_content_html(response_content)
    else:
        raise NotImplementedError()


def parse_reponse_content_plain_text(response_content:str) -> str:
    converted_text = response_content
    converted_text = converted_text.replace("\n", " ")
    converted_text = MULTI_SPACE_PATTERN.sub(" ", converted_text).strip()
    return converted_text


def parse_reponse_content_html(response_content:str) -> str:
    text_elements = BeautifulSoup(response_content).findAll(text=True)
    visible_elements = (elem.strip() for elem in text_elements if _elem_is_visible(elem))
    visible_text = " ".join(visible_elements)
    visible_text = visible_text.replace("\n", " ")
    visible_text = MULTI_SPACE_PATTERN.sub(" ", visible_text).strip()
    return visible_text


def _elem_is_visible(element) -> bool:
    # Thanks https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    if element.parent.name in NON_VISIBLE_TAGS:
        return False
    if isinstance(element, Comment):
        return False
    return True
