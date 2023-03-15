# Generated by Django 3.2.17 on 2023-03-15 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedbackdatauser_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackdatauser',
            options={'default_related_name': 'data_user', 'verbose_name': 'данные пользователя', 'verbose_name_plural': 'данные пользователя'},
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='data_user',
        ),
        migrations.AddField(
            model_name='feedbackdatauser',
            name='feedback',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_user', to='feedback.feedback', verbose_name='обратная связь'),
        ),
        migrations.AlterField(
            model_name='feedbackfiles',
            name='feedback',
            field=models.ForeignKey(default=None, help_text='прикрепите файлы', on_delete=django.db.models.deletion.CASCADE, related_name='files', to='feedback.feedback', verbose_name='обратная связь'),
        ),
    ]
