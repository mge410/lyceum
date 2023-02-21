# Generated by Django 3.2.17 on 2023-02-21 14:10

import catalog.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, validators=[django.core.validators.MaxValueValidator(32767, 'Максимальное число для ввода 32767')], verbose_name='вес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='В тексте должно быть одно из слов: роскошно, превосходно.', validators=[catalog.validators.perfect_validator], verbose_name='описание'),
        ),
    ]
