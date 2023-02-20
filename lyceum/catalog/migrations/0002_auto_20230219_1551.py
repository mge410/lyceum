# Generated by Django 3.2.17 on 2023-02-19 12:51

import re

import core.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(
                default=True, verbose_name='Опубликовано'
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(
                max_length=200,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile('^[-a-zA-Z0-9_]+\\Z'),
                        'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                        'invalid',
                    )
                ],
                verbose_name='Символьный код',
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.SmallIntegerField(default=100, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='catalog_items',
                to='catalog.category',
                verbose_name='Категория',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(
                default=True, verbose_name='Опубликовано'
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(
                to='catalog.Tag', verbose_name='Тэги'
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='Опишите товар',
                validators=[core.models.perfect_validate],
                verbose_name='Описание',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(
                default=True, verbose_name='Опубликовано'
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(
                max_length=200,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile('^[-a-zA-Z0-9_]+\\Z'),
                        'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                        'invalid',
                    )
                ],
                verbose_name='Символьный код',
            ),
        ),
    ]
