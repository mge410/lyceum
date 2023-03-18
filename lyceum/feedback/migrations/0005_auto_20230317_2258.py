# Generated by Django 3.2.17 on 2023-03-17 19:58

from django.db import migrations, models
import django.db.models.deletion
import feedback.models


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0004_auto_20230317_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={
                'ordering': ('created_at',),
                'verbose_name': 'mail',
                'verbose_name_plural': 'mails',
            },
        ),
        migrations.AlterModelOptions(
            name='feedbackfiles',
            options={
                'default_related_name': 'files',
                'verbose_name': 'feedback files',
                'verbose_name_plural': 'feedback files',
            },
        ),
        migrations.AlterModelOptions(
            name='feedbackuserdata',
            options={
                'default_related_name': 'data_user',
                'verbose_name': 'user data',
                'verbose_name_plural': 'users data',
            },
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(
                choices=[
                    ('c', 'accepted'),
                    ('b', 'processing'),
                    ('a', 'completed'),
                ],
                default='c',
                help_text='Mail status',
                max_length=2,
                verbose_name='status',
            ),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(
                help_text='Message to us', verbose_name='message to us'
            ),
        ),
        migrations.AlterField(
            model_name='feedbackfiles',
            name='feedback',
            field=models.ForeignKey(
                default=None,
                help_text='Attach files',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='files',
                to='feedback.feedback',
                verbose_name='feedback',
            ),
        ),
        migrations.AlterField(
            model_name='feedbackfiles',
            name='files',
            field=models.FileField(
                default=None,
                help_text='attach files',
                null=True,
                upload_to=feedback.models.FeedbackFiles.saving_path,
                verbose_name='files',
            ),
        ),
        migrations.AlterField(
            model_name='feedbackuserdata',
            name='email',
            field=models.EmailField(
                help_text='you need to enter a corrective email address',
                max_length=254,
                verbose_name='mail',
            ),
        ),
        migrations.AlterField(
            model_name='feedbackuserdata',
            name='feedback',
            field=models.OneToOneField(
                blank=True,
                help_text='Feedback',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='data_user',
                to='feedback.feedback',
                verbose_name='feedback',
            ),
        ),
    ]