import re
from functools import wraps
from typing import Any, Callable

from django.core import exceptions


def perfect_validator(*check_word_list: Any) -> Callable:
    @wraps(perfect_validator)
    def validate(value: str) -> None:
        value_word_list = re.split(r'\W', value)
        for word in value_word_list:
            for check_word in check_word_list:
                if check_word.lower() == word.lower():
                    return
        raise exceptions.ValidationError(
            f'В текста должно быть одно из слов: {check_word_list}, текст: {value}',
            params={'value': value},
        )

    return validate
