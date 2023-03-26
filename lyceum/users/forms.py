from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserChangeForm, UserCreationForm,
                                       UsernameField)
from django.db.models import Q

from users.models import Profile, UserProfileProxy

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
    )

    class Meta(UserCreationForm.Meta):
        model = UserProfileProxy
        fields = ('username', 'email')

    def clean_email(self):
        normalized_email = UserProfileProxy.objects.__class__.normalize_email(
            self.cleaned_data.get('email')
        )
        is_email_unique = UserProfileProxy.objects.filter(
            ~Q(pk=self.instance.id),
            email=normalized_email,
        ).exists()
        if is_email_unique:
            self.add_error(
                UserProfileProxy.email.field.name,
                'User with this email address is registered',
            )
        return normalized_email


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    password = None

    class Meta:
        model = UserProfileProxy
        field_classes = {'username': UsernameField}
        fields = [
            UserProfileProxy.email.field.name,
            UserProfileProxy.username.field.name,
            UserProfileProxy.first_name.field.name,
            UserProfileProxy.last_name.field.name,
        ]

    def clean_email(self):
        normalized_email = UserProfileProxy.objects.__class__.normalize_email(
            self.cleaned_data.get('email')
        )
        is_email_unique = UserProfileProxy.objects.filter(
            ~Q(pk=self.instance.id),
            email=normalized_email,
        ).exists()
        if is_email_unique:
            self.add_error(
                UserProfileProxy.email.field.name,
                'User with this email address is registered',
            )
        return normalized_email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            Profile.coffee_count.field.name,
            Profile.birthday.field.name,
            Profile.image.field.name,
        ]
        widgets = {
            Profile.coffee_count.field.name: forms.TextInput(
                attrs={'readonly': 'readonly'}
            ),
        }
