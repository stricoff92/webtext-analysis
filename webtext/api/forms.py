
from typing import Dict

from django import forms

from api.models import WebAnalysis
from api.utils import is_valid_url

class NewWebAnalysisForm(forms.Form):
    target_url = forms.CharField(max_length=300, required=True)
    analysis_mode = forms.CharField(max_length=8, required=True)

    def clean(self, *args, **kwargs) -> Dict:
        cleaned_data = super().clean(*args, **kwargs)
        analysis_mode = cleaned_data.get('analysis_mode', '')
        if analysis_mode not in WebAnalysis.ANALYSIS_MODES:
            raise forms.ValidationError("Invalid analysis_mode", code='invalid')

        target_url = cleaned_data.get('target_url', '')
        if not is_valid_url(target_url):
            raise forms.ValidationError("Invalid target_url", code='invalid')

        return cleaned_data
