import re
from typing import Any

from django.core.exceptions import ValidationError
from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text='Максимум 150 символов. Можно использовать'
        ' только буквы цифры и знаки подчеркивания и тире.',
        verbose_name='название',
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name[:15]


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('опубликовано', default=True)

    class Meta:
        abstract = True


class SluggedBaseModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Максимум 200 символов. Можно использовать'
        ' только буквы цифры и знаки подчеркивания и тире.',
        verbose_name='символьный код',
    )

    class Meta:
        abstract = True


class KeywordsBaseModel(models.Model):
    normalized_name = models.CharField(
        max_length=150,
        help_text='Нормализированное имя',
        verbose_name='Нормализированное имя',
        editable=False,
        null=True,
    )

    class Meta:
        abstract = True

    def clean(self, *args: Any, **kwargs: Any) -> None:
        normalized_name = self.get_normalized_name(self.name.lower())
        normalized_name_list = [
            item.normalized_name for item in self.__class__.objects.all()
        ]
        if normalized_name in normalized_name_list:
            raise ValidationError(
                'Уже есть обьект с похожем названием.'
                ' Перефразируйте ваш обьект или воспользуйтесь существующим'
            )
        self.normalized_name = normalized_name
        super(KeywordsBaseModel, self).clean()

    def get_normalized_name(self, text: str) -> str:
        replace_letters = {
            'e': 'е',
            'o': 'о',
            'c': 'с',
            'x': 'х',
            'a': 'а',
            'p': 'р',
            'y': 'у',
            't': 'т',
            'm': 'м',
            'k': 'к',
            'b': 'в',
        }
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])
            normalized_name = re.sub(r'\W', '', text)
        return normalized_name
