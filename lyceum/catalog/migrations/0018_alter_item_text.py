# Generated by Django 3.2.17 on 2023-03-28 11:00

from django.db import migrations
from django.db import models

import core.validators


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0017_auto_20230322_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='The text should contain one of the words: luxuriously, excellent.',
                validators=[
                    core.validators.ValidateMustContain(
                        'luxuriously', 'excellent'
                    )
                ],
                verbose_name='description',
            ),
        ),
    ]
