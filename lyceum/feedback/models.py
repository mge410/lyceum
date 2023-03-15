import core.models as core
from django.db import models


class Feedback(
    core.CreatedDateBaseModel,
    core.TextMessageModel,
):

    status = models.TextField(
        'статус',
        default='получено',
        choices=[
            ('получено', 'получено'),
            ('в обработке', 'в обработке'),
            ('ответ дан', 'ответ дан'),
        ],
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'


class FeedbackDataUser(models.Model):
    email = models.EmailField(
        'почта',
        max_length=254,
        help_text='необходимо ввести корректную почту',
    )

    feedback = models.OneToOneField(
        Feedback,
        verbose_name='обратная связь',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'данные пользователя'
        verbose_name_plural = 'данные пользователя'
        default_related_name = 'data_user'


class FeedbackFiles(models.Model):
    def saving_path(self, name):
        return f'uploads/{self.feedback.id}/{name}'

    files = models.FileField(
        'файлы',
        upload_to=saving_path,
        null=True,
        default=None,
    )

    feedback = models.ForeignKey(
        Feedback,
        verbose_name='обратная связь',
        on_delete=models.CASCADE,
        help_text='прикрепите файлы',
        default=None,
        related_name='files',
    )

    class Meta:
        verbose_name = 'файлы фидбека'
        verbose_name_plural = 'файлы фидбека'
        default_related_name = 'files'
