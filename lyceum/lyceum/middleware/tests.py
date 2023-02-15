from http import HTTPStatus

from django.test import Client, TestCase, override_settings


class StaticURLTests(TestCase):
    @override_settings(REVERSE_MIDDLEWARE='True')
    def test_middlevare_reverse_on_homepage(self) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                'append': 'lyceum.middleware.middleware.ReverseMiddleware',
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                client_self.get('/')
            response = client_self.get('/')
            self.assertContains(
                response,
                '<div>яанвалГ ацинартс</div>',
                status_code=HTTPStatus.OK,
            )

    @override_settings(REVERSE_MIDDLEWARE='True')
    def test_middlevare_reverse_on_catalog(self) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                'append': 'lyceum.middleware.middleware.ReverseMiddleware',
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                client_self.get('/catalog/')
            response = client_self.get('/catalog/')
            self.assertContains(
                response,
                '<div>косипС вотнемелэ</div>',
                status_code=HTTPStatus.OK,
            )

    @override_settings(REVERSE_MIDDLEWARE='False')
    def test_off_middlevare_reverse_on_catalog(self) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                'remove': 'lyceum.middleware.middleware.ReverseMiddleware',
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                client_self.get('/catalog/')
            response = client_self.get('/catalog/')
            self.assertContains(
                response,
                '<div>Список элементов</div>',
                status_code=HTTPStatus.OK,
            )
