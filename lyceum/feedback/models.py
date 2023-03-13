import core.models as core
from django.db import models


class Feedback(
    core.CreatedDateBaseModel,
    core.TextMessageModel,
):
    email = models.EmailField(
        max_length=254,
        verbose_name='Почта',
        help_text='Необходимо ввести корректную почту',
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'
