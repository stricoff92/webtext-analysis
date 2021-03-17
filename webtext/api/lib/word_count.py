
from collections import Counter
from typing import Dict


def get_word_counts(text:str) -> Dict:
    return dict(Counter(text.split(" ")))
