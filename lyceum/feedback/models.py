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
        help_text='статус письма',
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


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
        help_text='обратная связь',
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
        help_text='прикрепите файлы',
    )

    feedback = models.ForeignKey(
        Feedback,
        verbose_name='обратная связь',
        on_delete=models.CASCADE,
        default=None,
        related_name='files',
        help_text='прикрепите файлы',
    )

    class Meta:
        verbose_name = 'файлы фидбека'
        verbose_name_plural = 'файлы фидбека'
        default_related_name = 'files'
