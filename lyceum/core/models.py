from typing import Any, Callable

from django.core import exceptions
from django.db import models


def perfect_validate(*args: Any) -> Callable:
    def perfect_validator(value: str) -> None:
        for word in args:
            if str(word) in value.lower():
                return
        raise exceptions.ValidationError(
            f'В текста должно быть одно из слов {args}',
            params={'value': value},
        )

    return perfect_validator


class AbstractModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Имя', max_length=150)

    class Meta:
        abstract = True
