from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField
from users.models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    password = None

    class Meta:
        model = User
        field_classes = {'username': UsernameField}
        fields = [
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        ]


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
