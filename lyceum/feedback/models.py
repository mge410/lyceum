import core.models as core
from django.db import models


class Feedback(
    core.CreatedDateBaseModel,
    core.TextMessageModel,
):
    email = models.EmailField()

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'
