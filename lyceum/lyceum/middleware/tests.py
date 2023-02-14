from http import HTTPStatus

from django.conf import settings
from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_middlevare_reverse_on_homepage(self):
        if settings.REVERSE_MIDDLEWARE:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/')
                if count != 10:
                    self.assertContains(
                        response,
                        '<div>Главная страница</div>',
                        status_code=HTTPStatus.OK,
                    )
                else:
                    self.assertContains(
                        response,
                        '<div>яанвалГ ацинартс</div>',
                        status_code=HTTPStatus.OK,
                    )

    def test_middlevare_reverse_on_catalog(self):
        if settings.REVERSE_MIDDLEWARE:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/catalog/')
                if count != 10:
                    self.assertContains(
                        response,
                        '<div>Список элементов</div>',
                        status_code=HTTPStatus.OK,
                    )
                else:
                    self.assertContains(
                        response,
                        '<div>косипС вотнемелэ</div>',
                        status_code=HTTPStatus.OK,
                    )

    def test_off_middlevare_reverse_on_catalog(self):
        if settings.REVERSE_MIDDLEWARE is False:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/catalog/')
                self.assertContains(
                    response,
                    '<div>Список элементов</div>',
                    status_code=HTTPStatus.OK,
                )
