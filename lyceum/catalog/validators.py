import re
from typing import Any

from django.core import exceptions
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain:
    def __init__(self, *check_word_list: Any) -> None:
        self.check_word_list = list(
            map(lambda x: str(x).lower(), check_word_list)
        )

    def __call__(self, text: str) -> None:
        value_word_list = re.split(r'\W', text)
        for word in value_word_list:
            for check_word in self.check_word_list:
                if check_word == word.lower():
                    return
        raise exceptions.ValidationError(
            f'В текста должно быть одно из слов:'
            f' {self.check_word_list}, текст: {text}',
            params={'value': text},
        )
