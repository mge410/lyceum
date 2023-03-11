import re
from typing import Any, Callable

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail
from pytils import translit


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


class DateBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    image = models.ImageField(
        'Будут приведены к 300px',
        upload_to='catalog/',
    )

    class Meta:
        abstract = True

    def get_image_300x300(self) -> str:
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self) -> Callable | str:
        if self.image:
            return mark_safe(f'<img src="{self.get_image_300x300().url}">')
        return 'Нет изображения'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.image.name = '.'.join(list(map(lambda x: translit.slugify(x), self.image.name.split('.'))))
        super().save(*args, **kwargs)
        self.image = self.get_image_300x300()

    image_tmb.short_description = 'Изображение'


class NormalizedNameBaseModel(models.Model):
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
        normalized_name = self.get_normalized_name(self.name)
        normalized_name_list = [
            item.normalized_name for item in self.__class__.objects.all()
        ]
        if normalized_name in normalized_name_list:
            raise ValidationError(
                'Уже есть обьект с похожем названием.'
                ' Перефразируйте ваш обьект или воспользуйтесь существующим'
            )
        self.normalized_name = normalized_name
        super(NormalizedNameBaseModel, self).clean()

    def get_normalized_name(self, text: str) -> str:
        replace_letters = {
            'e': 'е',
            'o': 'о',
            'c': 'с',
            'x': 'х',
            'a': 'а',
            'p': 'р',
            'y': 'у',
            'A': 'А',
            'P': 'Р',
            'C': 'С',
            'E': 'Е',
            'O': 'О',
            'X': 'Х',
            'T': 'Т',
            'M': 'М',
            'K': 'К',
            'B': 'В',
            'H': 'Н',
        }
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])
            normalized_name = re.sub(r'\W', '', text).lower()
        return normalized_name
