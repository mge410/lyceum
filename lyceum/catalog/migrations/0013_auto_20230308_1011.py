# Generated by Django 3.2.17 on 2023-03-08 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_item_is_on_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'default_related_name': 'items', 'ordering': ('name',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]