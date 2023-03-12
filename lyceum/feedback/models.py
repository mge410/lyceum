import core.models as core
from django.db import models


class Feedback (
    core.CreatedDateBaseModel,
    core.TextBaseModel,
):
    email = models.EmailField()

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self) -> str:
        return self.email[:20]
