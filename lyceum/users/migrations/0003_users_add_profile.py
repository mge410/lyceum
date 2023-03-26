# Generated by Django 3.2.17 on 2023-03-21 11:17
from django.contrib.auth.models import User
from django.db import migrations, transaction

from users.models import Profile


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    def fill_users_profile(apps, schema_editor):
        db_alias = schema_editor.connection.alias

        with transaction.atomic():
            for user in User.objects.using(db_alias).all():
                profile = Profile(user=user)
                profile.save()

    def delete_users_profile(apps, schema_editor):
        db_alias = schema_editor.connection.alias

        with transaction.atomic():
            for user in User.objects.using(db_alias).all():
                if hasattr(user, 'profile'):
                    profile = Profile.objects.get(user=user)
                    profile.delete()

    operations = [
        migrations.RunPython(
            fill_users_profile,
            reverse_code=delete_users_profile,
        )
    ]
