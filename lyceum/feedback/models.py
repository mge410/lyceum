from django.db import models

import core.models as core


class Feedback(
    core.CreatedDateBaseModel,
    core.TextMessageModel,
):
    class Status(models.TextChoices):
        accepted = 'c', 'accepted'
        processing = 'b', 'processing'
        completed = 'a', 'completed'

    status = models.CharField(
        'status',
        max_length=2,
        default=Status.accepted,
        choices=Status.choices,
        help_text='Mail status',
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'mail'
        verbose_name_plural = 'mails'


class FeedbackUserData(models.Model):
    email = models.EmailField(
        'mail',
        max_length=254,
        help_text='you need to enter a corrective email address',
    )

    feedback = models.OneToOneField(
        Feedback,
        on_delete=models.CASCADE,
        verbose_name='feedback',
        null=True,
        blank=True,
        help_text='Feedback',
    )

    class Meta:
        verbose_name = 'user data'
        verbose_name_plural = 'users data'
        default_related_name = 'data_user'


class FeedbackFiles(models.Model):
    def saving_path(self, name):
        return f'uploads/{self.feedback.id}/{name}'

    files = models.FileField(
        'files',
        upload_to=saving_path,
        null=True,
        default=None,
        help_text='attach files',
    )

    feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        verbose_name='feedback',
        default=None,
        related_name='files',
        help_text='Attach files',
    )

    class Meta:
        verbose_name = 'feedback files'
        verbose_name_plural = 'feedback files'
        default_related_name = 'files'
