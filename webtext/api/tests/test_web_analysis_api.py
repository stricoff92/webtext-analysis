
import json
from unittest.mock import patch

from django.urls import reverse
from django.test import override_settings
import requests
from rest_framework import status

from api.models import WebAnalysis
from api.lib.content_types import (
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_HTML,
)
from .base_test_case import BaseTestBase
from .factory import MockHTTPResponse


class WebAnalysisAPITests(BaseTestBase):

    def setUp(self):
        super().setUp()
        self.mock_requests_get = patch.object(requests, "get").start()

    def tearDown(self):
        self.mock_requests_get.stop()
        super().tearDown()


    def test_user_can_create_new_web_analysis_for_static_plain_test_page(self):
        """ Test a user can create a new web analysis for a static plain text page
        """
        self.client.force_login(self.user)

        # Prepare mock response
        mock_status_code = status.HTTP_200_OK
        mock_response_headers = {
            'content-type':CONTENT_TYPE_TEXT,
        }
        mock_response_content = b'Sitemap: https://www.foobar.com/sitemaps/\nUser-agent: *'
        mock_response = MockHTTPResponse(
            status.HTTP_200_OK, mock_response_content, headers=mock_response_headers)
        self.mock_requests_get.return_value = mock_response

        # Call API to scape data and analyze page
        target_url = 'https://foobar.com/robots.txt'
        api_url = reverse("api-create-web-analysis")
        data = {
            'target_url':target_url,
            'analysis_mode':WebAnalysis.ANALYSIS_MODE_STATIC,
        }
        response = self.client.post(api_url, data, format="json")

        # Validate data returned from the API
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['created_at'])
        self.assertIsNotNone(response.data['slug'])
        self.assertEqual(response.data['target_url'], target_url)
        self.assertEqual(response.data['page_content_type'], CONTENT_TYPE_TEXT)
        self.assertEqual(response.data['analysis_mode'], WebAnalysis.ANALYSIS_MODE_STATIC)
        self.assertEqual(response.data['page_content_length'], 55)
        self.assertEqual(
            response.data['word_counts'],
            {'Sitemap:': 1, 'https://www.foobar.com/sitemaps/': 1, 'User-agent:': 1, '*': 1})


    def test_user_can_save_new_web_analysis_record_to_the_database(self):
        """ Test a database record is saved when a user creates a new web analysis.
        """
        self.client.force_login(self.user)

        # Prepare mock response
        mock_status_code = status.HTTP_200_OK
        mock_response_headers = {
            'content-type':CONTENT_TYPE_TEXT,
        }
        mock_response_content = b'Sitemap: https://www.foobar.com/sitemaps/\nUser-agent: *'
        mock_response = MockHTTPResponse(
            status.HTTP_200_OK, mock_response_content, headers=mock_response_headers)
        self.mock_requests_get.return_value = mock_response

        # Call API to scape data and analyze page
        target_url = 'https://foobar.com/robots.txt'
        api_url = reverse("api-create-web-analysis")
        data = {
            'target_url':target_url,
            'analysis_mode':WebAnalysis.ANALYSIS_MODE_STATIC,
        }
        response = self.client.post(api_url, data, format="json")

        # Validate a new database record was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WebAnalysis.objects.count(), 1)

        web_analysis = WebAnalysis.objects.first()
        self.assertIsNotNone(web_analysis.slug)
        self.assertIsNotNone(web_analysis.created_at)
        self.assertEqual(web_analysis.owner, self.user)
        self.assertEqual(web_analysis.target_url, target_url)
        self.assertEqual(web_analysis.page_content_length, 55)
        self.assertEqual(web_analysis.page_content_type, CONTENT_TYPE_TEXT)
        self.assertEqual(web_analysis.page_content, "Sitemap: https://www.foobar.com/sitemaps/ User-agent: *")


    def test_valid_url_is_required_to_create_new_web_analysis(self):
        """ Test a valid url is required when creating a new web analysis
        """
        self.client.force_login(self.user)

        # url that doesnt start with "http"
        target_url = 'not-a-valid-url.com'
        api_url = reverse("api-create-web-analysis")
        data = {
            'target_url':target_url,
            'analysis_mode':WebAnalysis.ANALYSIS_MODE_STATIC,
        }
        response = self.client.post(api_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.data),
            {"__all__": [{"message": "Invalid target_url", "code": "invalid"}]})

        # url with a non ascii char
        target_url = f'https://url-with-non-ascii-char-{chr(3234)}.com'
        data = {
            'target_url':target_url,
            'analysis_mode':WebAnalysis.ANALYSIS_MODE_STATIC,
        }
        response = self.client.post(api_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.data),
            {"__all__": [{"message": "Invalid target_url", "code": "invalid"}]})

        # url with no TLD
        target_url = f'https://url-with-no-tld'
        data = {
            'target_url':target_url,
            'analysis_mode':WebAnalysis.ANALYSIS_MODE_STATIC,
        }
        response = self.client.post(api_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.data),
            {"__all__": [{"message": "Invalid target_url", "code": "invalid"}]})


    def test_valid_analysis_mode_is_required_to_create_new_web_analysis(self):
        """ Test a valid analysis mode is required when creating a new web analysis
        """
        self.client.force_login(self.user)

        target_url = 'https://foobar.com/robots.txt'
        api_url = reverse("api-create-web-analysis")
        data = {
            'target_url':target_url,
            'analysis_mode':'invalid-analysis',
        }
        response = self.client.post(api_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("Invalid analysis_mode" in str(response.data)) # TODO: fix json formatting


    def test_user_can_get_web_analysis_details_for_their_own_web_analysis(self):
        """ Test a user can get details of their own web analysis.
        """
        self.client.force_login(self.user)

        page_content_length = 42
        web_analysis = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')

        api_url = reverse("api-get-web-analysis-details", kwargs={'slug':web_analysis.slug})
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['slug'], web_analysis.slug)
        self.assertEqual(response.data['target_url'], web_analysis.target_url)
        self.assertEqual(response.data['page_content_length'], page_content_length)
        self.assertEqual(response.data['page_content_type'], CONTENT_TYPE_TEXT)
        self.assertEqual(response.data['analysis_mode'], WebAnalysis.ANALYSIS_MODE_STATIC)
        self.assertEqual(response.data['page_content'], 'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *')
        self.assertEqual(
            response.data['word_counts'],
            {'Sitemap:': 1, 'https://www.foobar.com/sitemaps/': 1, 'User-agent:': 1, '*': 1})


    def test_user_can_get_web_analysis_details_for_other_users_web_analysis(self):
        """ Test a user cant get details of another user's web analysis.
        """
        self.client.force_login(self.user)

        page_content_length = 42
        web_analysis = self.factory.create_web_analysis(
            self.other_user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')

        # user has no access
        api_url = reverse("api-get-web-analysis-details", kwargs={'slug':web_analysis.slug})
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # other user has access
        self.client.force_login(self.other_user)
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_can_get_web_analysis_list_for_their_own_web_analysis(self):
        """ Test a user can get list of their own web analysis.
        """
        self.client.force_login(self.user)

        page_content_length = 42
        web_analysis1 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')
        web_analysis2 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')

        api_url = reverse("api-get-web-analysis-list")
        response = self.client.get(api_url + "?page=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['rows']), 2)

        returned_slugs = [wa['slug'] for wa in response.data['rows']]
        self.assertTrue(web_analysis1.slug in returned_slugs)
        self.assertTrue(web_analysis2.slug in returned_slugs)
        self.assertFalse(response.data['another_page'])


    def test_user_cant_get_web_analysis_list_for_other_users_web_analysis(self):
        """ Test a user cant get list of other users web analysis.
        """
        self.client.force_login(self.other_user)

        page_content_length = 42
        web_analysis1 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')
        web_analysis2 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')

        api_url = reverse("api-get-web-analysis-list")
        response = self.client.get(api_url + "?page=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['rows']), 0) # No records returned.
        self.assertFalse(response.data['another_page'])


    @override_settings(PAGINATION_PAGE_SIZE=1)
    def test_user_can_paginate_through_list_of_their_own_web_analysis(self):
        """ Test a user can paginate through a list of their own web analysis details
        """
        self.client.force_login(self.user)

        page_content_length = 42
        web_analysis1 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')
        web_analysis2 = self.factory.create_web_analysis(
            self.user,
            'Sitemap: https://www.foobar.com/sitemaps/ User-agent: *',
            page_content_length,
            'https://foobar.com/robots.txt')

        api_url = reverse("api-get-web-analysis-list")

        response = self.client.get(api_url + "?page=1&sort=created_at")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['rows']), 1)
        self.assertTrue(response.data['another_page'])
        returned_slugs_page_1 = [wa['slug'] for wa in response.data['rows']]
        self.assertTrue(web_analysis1.slug in returned_slugs_page_1)
        self.assertFalse(web_analysis2.slug in returned_slugs_page_1)
        self.assertTrue(response.data['another_page'])

        response = self.client.get(api_url + "?page=2&sort=created_at")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['rows']), 1)
        self.assertTrue(response.data['another_page'])
        returned_slugs_page_2 = [wa['slug'] for wa in response.data['rows']]
        self.assertFalse(web_analysis1.slug in returned_slugs_page_2)
        self.assertTrue(web_analysis2.slug in returned_slugs_page_2)
        self.assertTrue(response.data['another_page'])

        response = self.client.get(api_url + "?page=3&sort=created_at")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['rows']), 0)
        self.assertFalse(response.data['another_page'])
