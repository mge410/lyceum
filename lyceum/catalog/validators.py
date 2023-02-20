from functools import wraps
from typing import Any, Callable

from django.core import exceptions


def perfect_validator(*args: Any) -> Callable:
    @wraps(perfect_validator)
    def validate(value: str) -> None:
        for word in args:
            if str(word) in value.lower():
                return
        raise exceptions.ValidationError(
            f'В текста должно быть одно из слов {args}',
            params={'value': value},
        )

    return validate
