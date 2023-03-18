# Generated by Django 3.2.17 on 2023-03-17 19:58

import core.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0014_auto_20230308_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='galleryimagesitem',
            options={
                'default_related_name': 'gallery_images',
                'verbose_name': 'image',
                'verbose_name_plural': 'image gallery',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={
                'default_related_name': 'items',
                'ordering': ('name',),
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AlterModelOptions(
            name='mainimageitem',
            options={
                'default_related_name': 'main_image',
                'verbose_name': 'main image',
                'verbose_name_plural': 'main images',
            },
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={
                'default_related_name': 'tags',
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(
                help_text='Maximum 150 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=150,
                unique=True,
                verbose_name='name',
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='normalized_name',
            field=models.CharField(
                editable=False,
                help_text='Normalized name',
                max_length=150,
                null=True,
                verbose_name='normalized name',
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(
                help_text='Maximum 200 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=200,
                unique=True,
                verbose_name='slug',
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(
                default=100,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, 'Minimum number to enter 0'
                    ),
                    django.core.validators.MaxValueValidator(
                        32767, 'The maximum number to enter is 32767'
                    ),
                ],
                verbose_name='weight',
            ),
        ),
        migrations.AlterField(
            model_name='galleryimagesitem',
            name='image',
            field=models.ImageField(
                upload_to='catalog/', verbose_name='Will be rendered at 300px'
            ),
        ),
        migrations.AlterField(
            model_name='galleryimagesitem',
            name='item',
            field=models.ForeignKey(
                blank=True,
                help_text='gallery images',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='gallery_images',
                to='catalog.item',
                verbose_name='gallery images',
            ),
        ),
        migrations.AlterField(
            model_name='galleryimagesitem',
            name='name',
            field=models.CharField(
                help_text='Maximum 150 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=150,
                unique=True,
                verbose_name='name',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(
                help_text='The product must have a category.',
                on_delete=django.db.models.deletion.PROTECT,
                related_name='items',
                to='catalog.category',
                verbose_name='category',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(
                default=False, verbose_name='Show on home page'
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(
                help_text='Maximum 150 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=150,
                unique=True,
                verbose_name='name',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(
                help_text='The element must have at least 1 tag.',
                related_name='items',
                to='catalog.Tag',
                verbose_name='tags',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='The text should contain one of the words: luxurious, excellent.',
                validators=[
                    core.validators.ValidateMustContain(
                        'luxuriously', 'excellent'
                    )
                ],
                verbose_name='description',
            ),
        ),
        migrations.AlterField(
            model_name='mainimageitem',
            name='image',
            field=models.ImageField(
                upload_to='catalog/', verbose_name='Will be rendered at 300px'
            ),
        ),
        migrations.AlterField(
            model_name='mainimageitem',
            name='items',
            field=models.OneToOneField(
                blank=True,
                help_text='main image',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='main_image',
                to='catalog.item',
                verbose_name='main image',
            ),
        ),
        migrations.AlterField(
            model_name='mainimageitem',
            name='name',
            field=models.CharField(
                help_text='Maximum 150 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=150,
                unique=True,
                verbose_name='name',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(
                help_text='Maximum 150 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=150,
                unique=True,
                verbose_name='name',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='normalized_name',
            field=models.CharField(
                editable=False,
                help_text='Normalized name',
                max_length=150,
                null=True,
                verbose_name='normalized name',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(
                help_text='Maximum 200 characters. Only letters, numbers, underscores, and dashes can be used.',
                max_length=200,
                unique=True,
                verbose_name='slug',
            ),
        ),
    ]
