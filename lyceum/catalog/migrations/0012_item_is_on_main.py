# Generated by Django 3.2.17 on 2023-03-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0011_alter_galleryimagesitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(
                default=False, verbose_name='Отображать на главной'
            ),
        ),
    ]