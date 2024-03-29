# Generated by Django 3.2.17 on 2023-03-22 11:47

from django.db import migrations
from django.db import models

import catalog.models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0015_auto_20230317_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimagesitem',
            name='image',
            field=models.ImageField(
                upload_to=catalog.models.GalleryImagesItem.saving_path,
                verbose_name='Will be rendered at 300px',
            ),
        ),
        migrations.AlterField(
            model_name='mainimageitem',
            name='image',
            field=models.ImageField(
                upload_to=catalog.models.MainImageItem.saving_path,
                verbose_name='Will be rendered at 300px',
            ),
        ),
    ]
