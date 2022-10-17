from rest_framework import status
from rest_framework.reverse import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
import pdb


class TestDuckSearchView(APITestCase):
    def test_search_query(self):
        response = self.client.get(reverse("duck-search"), {"query": "latest news"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_no_of_pages_to_scrape(self):
        response = self.client.get(
            reverse("duck-search"), {"query": "latest news", "pages": 2}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # having position > 10 in response means more than 1 pages were scraped
        self.assertContains(response, '"position":15')
