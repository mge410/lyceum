from http import HTTPStatus

from django.test import Client
from django.test import TestCase


class StaticURLTests(TestCase):
    def test_feedback_endpoint(self) -> None:
        response = Client().get('/feedback/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
