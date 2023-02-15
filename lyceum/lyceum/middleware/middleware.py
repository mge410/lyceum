import re

from django.http import HttpResponse


class ReverseMiddleware:
    regular = r'[а-яА-Я]'

    def __init__(self, get_response):
        self.count = 0
        self.get_response = get_response

    def __call__(self, request: HttpResponse) -> HttpResponse:
        self.count += 1
        response = self.get_response(request)

        if self.count % 10 != 0:
            return response

        response.content = self.reverse_word_cyrillic(
            list(response.content.decode('utf-8'))
        )
        return response

    @classmethod
    def reverse_word_cyrillic(cls, text: list) -> str:
        letter_cyrillic_flag = False
        letter_cyrillic_index = 0

        for index, letter in enumerate(text):
            if (
                letter_cyrillic_flag is False
                and re.match(cls.regular, letter) is not None
            ):
                letter_cyrillic_flag = True
                letter_cyrillic_index = index
            elif (
                letter_cyrillic_flag is True
                and re.match(cls.regular, letter) is None
            ):
                text[letter_cyrillic_index:index] = text[
                    letter_cyrillic_index:index:
                ][::-1]
                letter_cyrillic_flag = False
            elif index + 1 == len(text) and letter_cyrillic_flag is True:
                if re.match(cls.regular, letter) is None:
                    text[letter_cyrillic_index:index] = text[
                        letter_cyrillic_index:index:
                    ][::-1]
                else:
                    text[letter_cyrillic_index : index + 1] = text[
                        letter_cyrillic_index : index + 1 :
                    ][::-1]
        return ''.join(text)
