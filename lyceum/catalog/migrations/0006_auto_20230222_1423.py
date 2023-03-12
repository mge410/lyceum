# Generated by Django 3.2.17 on 2023-02-22 11:23

import core.validators
import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0005_auto_20230221_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={
                'default_related_name': 'tags',
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(
                help_text='Максимум 150 символов. Можно использовать только буквы цифры и знаки подчеркивания и тире.',
                max_length=150,
                unique=True,
                verbose_name='название',
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(
                default=100,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, 'Минимальное число для ввода 0'
                    ),
                    django.core.validators.MaxValueValidator(
                        32767, 'Максимальное число для ввода 32767'
                    ),
                ],
                verbose_name='вес',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(
                help_text='Максимум 150 символов. Можно использовать только буквы цифры и знаки подчеркивания и тире.',
                max_length=150,
                unique=True,
                verbose_name='название',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='В тексте должно быть одно из слов: роскошно, превосходно.',
                validators=[
                    core.validators.ValidateMustContain(
                        'роскошно', 'превосходно'
                    )
                ],
                verbose_name='описание',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(
                help_text='Максимум 150 символов. Можно использовать только буквы цифры и знаки подчеркивания и тире.',
                max_length=150,
                unique=True,
                verbose_name='название',
            ),
        ),
    ]
