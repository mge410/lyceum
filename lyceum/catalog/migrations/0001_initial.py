# Generated by Django 3.2.17 on 2023-02-19 06:33

import re

import django.core.validators
from django.db import migrations
from django.db import models
import django.db.models.deletion

from core.validators import ValidateMustContain


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                (
                    'slug',
                    models.CharField(
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^[-a-zA-Z0-9_]+\\Z'),
                                'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                                'invalid',
                            ),
                            ValidateMustContain,
                        ],
                    ),
                ),
                ('weight', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                (
                    'slug',
                    models.CharField(
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^[-a-zA-Z0-9_]+\\Z'),
                                'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.',
                                'invalid',
                            )
                        ],
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='catalog_items',
                        to='catalog.category',
                    ),
                ),
                ('tags', models.ManyToManyField(to='catalog.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
