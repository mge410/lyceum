# Generated by Django 3.2.17 on 2023-03-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.TextField(choices=[('получено', 'получено'), ('в обработке', 'в обработке'), ('ответ дан', 'ответ дан')], default='получено', verbose_name='статус'),
        ),
    ]
