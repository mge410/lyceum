import re
from typing import Any

from django.http import HttpRequest, HttpResponse


class ReverseMiddleware:
    regular_split = r'\W|[0-9]'
    regular_check = r'^[А-ЯЁа-яё]*$'

    def __init__(self, get_response: Any):
        self.count = 0
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        self.count += 1
        response = self.get_response(request)

        if self.count % 10 != 0:
            return response

        response.content = self.reverse_word_cyrillic(
            response.content.decode('utf-8')
        )
        return response

    @classmethod
    def reverse_word_cyrillic(cls, text: str) -> str:
        word_list = re.split(cls.regular_split, text)

        for word in word_list:
            if re.fullmatch(cls.regular_check, word):
                text = text.replace(word, word[::-1], 2)

        return text
