
from collections import Counter
from itertools import chain

from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from api.forms import NewWebAnalysisForm
from api.lib import (
    web_scraper as scraper_lib,
    web_parser as parser_lib,
    word_count
)
from api.models import WebAnalysis


class WebAnalysisBasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebAnalysis
        fields = ('slug', 'created_at', 'target_url', 'page_content_length', 'page_content_type', 'analysis_mode')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_web_analysis(request):
    """ Fetch a URL and return an analysis of the text
    """
    form = NewWebAnalysisForm(request.data)

    if not form.is_valid():
        return Response(
            form.errors.as_json(), status.HTTP_400_BAD_REQUEST)

    target_url = form.cleaned_data['target_url']
    analysis_mode = form.cleaned_data['analysis_mode']

    # Download content that URL points to.
    try:
        (page_content, page_content_type) = scraper_lib.scrape_page(
            target_url, analysis_mode)
    except scraper_lib.WebScrapeError as e:
        return Response({'error':str(e)}, status.HTTP_502_BAD_GATEWAY) # TODO: is 502 ok here?

    # Convert content to plain text.
    parsed_content = parser_lib.parse_resonse_content(
        page_content, page_content_type)

    # analyze text
    word_counts = word_count.get_word_counts(parsed_content)

    # save text content to the datadase and build reponse payload.
    new_web_analysis = WebAnalysis.objects.create(
        owner=request.user,
        target_url=target_url,
        page_content=parsed_content,
        page_content_length=len(parsed_content),
        page_content_type=page_content_type,
        analysis_mode=analysis_mode)

    data = WebAnalysisBasicDetailsSerializer(new_web_analysis).data
    data['page_content'] = parsed_content
    data['word_counts'] = word_counts
    return Response(data, status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_web_analysis_details(request, slug):
    """ Get details of a previously fetched url
    """
    web_analysis = get_object_or_404(
        WebAnalysis, owner=request.user, slug=slug)

    data = WebAnalysisBasicDetailsSerializer(web_analysis).data
    data['page_content'] = web_analysis.page_content
    data['word_counts'] = word_count.get_word_counts(web_analysis.page_content)
    return Response(data, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_web_analysis_list(request):
    """ Get list of a previously fetched urls
    """
    # Get pagination info from query params.
    try:
        page = abs(int(request.query_params.get("page", 1)))
    except ValueError:
        return Response("invalid pagination page", status.HTTP_400_BAD_REQUEST)
    page_size = settings.PAGINATION_PAGE_SIZE
    start_ix = (page - 1) * page_size
    end_ix = start_ix + page_size

    # Get sort info from query params.
    sortable_columns = ['created_at', 'page_content_length',]
    sortable_columns = list(chain(*list([f"{v}", f"-{v}"] for v in sortable_columns)))
    sort_by = request.query_params.get("sort", '-created_at')

    # Apply sorting and pagination.
    qs = WebAnalysis.objects.filter(owner=request.user).order_by(sort_by)
    qs = qs[start_ix:end_ix]

    data = {}
    data['rows'] = WebAnalysisBasicDetailsSerializer(qs, many=True).data
    data['another_page'] = qs.count() == page_size
    return Response(data, status.HTTP_200_OK)
