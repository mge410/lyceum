# Generated by Django 3.2.17 on 2023-02-20 18:52

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_auto_20230220_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='В тексте должно быть одно из слов: роскошно, превосходно.',
                validators=[catalog.validators.perfect_validator],
                verbose_name='описание',
            ),
        ),
    ]
