from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.db.models import Q
from users.models import Profile
from users.models import UserProfileProxy

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
    )

    class Meta(UserCreationForm.Meta):
        model = UserProfileProxy
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        is_email_unique = UserProfileProxy.objects.filter(
            email=cleaned_data['email']
        ).exists()
        if is_email_unique:
            self.add_error(
                UserProfileProxy.email.field.name,
                'User with this email address is registered',
            )


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

    def clean(self):
        cleaned_data = super().clean()
        is_email_unique = UserProfileProxy.objects.filter(
            ~Q(pk=self.instance.id),
            email=UserProfileProxy.get_normalized_email(cleaned_data['email']),
        ).exists()
        if is_email_unique:
            self.add_error(
                UserProfileProxy.email.field.name,
                'User with this email address is registered',
            )
        cleaned_data['email'] = UserProfileProxy.get_normalized_email(
            cleaned_data['email']
        )


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
