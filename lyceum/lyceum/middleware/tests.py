from django.test import Client, TestCase, override_settings
from parameterized import parameterized


class StaticURLTests(TestCase):
    @parameterized.expand(
        [
            ['/', '<div>яанвалГ ацинартс</div>'],
            ['/catalog/', '<div>косипС вотнемелэ</div>'],
            ['/catalog/2/', '<div>онбордоП тнемелэ id: 2</div>'],
            ['/about/', '<div>О еткеорп</div>'],
        ]
    )
    @override_settings(REVERSE_MIDDLEWARE='True')
    def test_middlevare_reverse_on_homepage(self, url: str, text: str) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                'append': 'lyceum.middleware.middleware.ReverseMiddleware',
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                client_self.get(f'{url}')
            response = client_self.get(f'{url}')
            self.assertEqual(
                response.content.decode('utf-8'),
                f'{text}',
                f'Expected: {text}, '
                f'got: {response.content.decode("utf-8")}, testcase: {url}',
            )

    @parameterized.expand(
        [
            ['/', '<div>Главная страница</div>'],
            ['/catalog/', '<div>Список элементов</div>'],
            ['/catalog/2/', '<div>Подробно элемент id: 2</div>'],
            ['/about/', '<div>О проекте</div>'],
        ]
    )
    @override_settings(REVERSE_MIDDLEWARE='False')
    def test_off_middlevare_reverse_on_catalog(
        self, url: str, text: str
    ) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                'remove': 'lyceum.middleware.middleware.ReverseMiddleware',
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                client_self.get(f'{url}')
            response = client_self.get(f'{url}')
            self.assertEqual(
                response.content.decode('utf-8'),
                f'{text}',
                f'Expected: {text}, '
                f'got: {response.content.decode("utf-8")}, testcase: {url}',
            )
