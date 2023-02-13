from django.conf import settings
from django.test import Client, TestCase
from http import HTTPStatus


class StaticURLTests(TestCase):
    def test_middlevare_reverse_on_homepage(self):
        if settings.REVERSE_MIDDLEWARE:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/')
                if count != 10:
                    self.assertContains(
                        response,
                        '<div><h1>Главная страница</h1></div>',
                        status_code=HTTPStatus.OK,
                    )
                else:
                    self.assertContains(
                        response,
                        '<div><h1>яанвалГ ацинартс</h1></div>',
                        status_code=HTTPStatus.OK,
                    )

    def test_middlevare_reverse_on_catalog(self):
        if settings.REVERSE_MIDDLEWARE:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/catalog/')
                if count != 10:
                    self.assertContains(
                        response, '<body>Список элементов</body>', status_code=HTTPStatus.OK
                    )
                else:
                    self.assertContains(
                        response, '<body>косипС вотнемелэ</body>', status_code=HTTPStatus.OK
                    )

    def test_off_middlevare_reverse_on_catalog(self):
        if settings.REVERSE_MIDDLEWARE is False:
            client_self = Client()
            for count in range(1, 11):
                response = client_self.get('/catalog/')
                self.assertContains(
                    response, '<body>Список элементов</body>', status_code=HTTPStatus.OK
                )
