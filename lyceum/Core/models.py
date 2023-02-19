from django.core import exceptions
from django.db import models


def perfect_validate(value: str) -> None:
    if 'превосходно' not in value.lower() and 'роскошно' not in value.lower():
        raise exceptions.ValidationError(
            'В текста должно быть слово превосходно или роскошно',
            params={'value': value},
        )


class AbstractModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Имя', max_length=150)

    class Meta:
        abstract = True
