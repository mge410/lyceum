import re

from django.test import Client
from django.test import override_settings
from django.test import TestCase
from parameterized import parameterized


class ReverseMiddlewareTests(TestCase):
    @parameterized.expand(
        [
            ["/catalog/"],
            ["/about/"],
        ]
    )
    @override_settings(REVERSE_MIDDLEWARE="True")
    def test_middlevare_reverse(self, url: str) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                "append": "lyceum.middleware.middleware.ReverseMiddleware",
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                response = client_self.get(f"{url}")

            text = response.content.decode("utf-8")
            word_list = re.split(r"\W|[0-9]", response.content.decode("utf-8"))

            for word in word_list:
                if re.fullmatch(r"^[А-ЯЁа-яё]*$", word):
                    text = text.replace(word, word[::-1], 2)

            response_reverse = client_self.get(f"{url}")
            self.assertEqual(
                response_reverse.content.decode("utf-8"),
                f"{text}",
                f'Expected: {text}, '
                f'got: {response_reverse.content.decode("utf-8")},'
                f' testcase: {url}',
            )

    @parameterized.expand(
        [
            ["/catalog/"],
            ["/about/"],
        ]
    )
    @override_settings(REVERSE_MIDDLEWARE="False")
    def test_off_middlevare_reverse(self, url: str) -> None:
        with self.modify_settings(
            MIDDLEWARE={
                "remove": "lyceum.middleware.middleware.ReverseMiddleware",
            }
        ):
            client_self = Client()
            for count in range(1, 10):
                response = client_self.get(f"{url}")
            response_reverse = client_self.get(f"{url}")
            self.assertEqual(
                response_reverse.content.decode("utf-8"),
                f'{response.content.decode("utf-8")}',
                f'Expected: {response.content.decode("utf-8")}, '
                f'got: {response_reverse.content.decode("utf-8")},'
                f' testcase: {url}',
            )
