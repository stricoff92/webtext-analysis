
from itertools import chain

from django.db import models
from django.contrib.auth import get_user_model

from api.utils import generate_slug


class WebAnalysis(models.Model):

    slug = models.SlugField(unique=True, editable=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    target_url = models.URLField(max_length=300)
    page_content = models.TextField()
    page_content_length = models.PositiveIntegerField()
    page_content_type = models.CharField(max_length=30)

    ANALYSIS_MODE_STATIC = 'static'
    ANALYSIS_MODES = (ANALYSIS_MODE_STATIC, )
    ANALYSIS_MODES_CHOICES = (
        (ANALYSIS_MODE_STATIC, "Static",),
    )
    analysis_mode = models.CharField(max_length=8, choices=ANALYSIS_MODES_CHOICES)


    def __str__(self):
        return f"<WebAnalysis {self.id} ({self.target_url[:12]}{'...' if len(self.target_url) > 12 else ''})>"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(WebAnalysis)
            if 'update_fields' in kwargs and 'slug' not in kwargs['update_fields']:
                kwargs['update_fields'] = list(chain(kwargs['update_fields'], ['slug']))

        return super().save(*args, **kwargs)
