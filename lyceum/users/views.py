from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

import users.forms
from users.models import Profile
from users.models import UserProfileProxy


class Register(View):
    template_name = 'users/signup.html'

    def get(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        context = {'form': users.forms.CustomUserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = users.forms.CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = settings.DEFAULT_USER_ACTIVITY
            user.save()
            profile = Profile(user=user)
            profile.save()

            if not settings.DEFAULT_USER_ACTIVITY:
                absolute_url = self.request.build_absolute_uri(
                    reverse_lazy(
                        'users:activate',
                        args=[user.username],
                    )
                )
                send_mail(
                    'Email verification',
                    f'Thank you for registering on our website! <br>'
                    f'Profile activation link! <br>'
                    f'- « {absolute_url}',
                    settings.MAIL_SENDER,
                    [f'{form.cleaned_data["email"]}'],
                    fail_silently=False,
                )

            return redirect('homepage:home')
        context = {'form': form}
        return render(request, self.template_name, context)


class ActivateUsers(View):
    template_name = 'users/activate.html'

    def get(self, request: HttpRequest, name: str) -> HttpResponse:
        context = {}

        user = get_object_or_404(User, username=name)
        if (
            user.date_joined < timezone.now() - timedelta(hours=12)
            and not user.is_active
        ):
            user.delete()
            messages.error(request, 'Overdue =(')
        elif user.is_active is False:
            user.is_active = True
            user.save()
            messages.success(
                request, 'Your account has been' ' successfully activated'
            )
        else:
            messages.success(request, 'This user is already activated')

        return render(request, self.template_name, context)


class UsersList(View):
    template_name = 'users/user_list.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        users = UserProfileProxy.objects.get_user_list()
        context = {'users': users}
        return render(request, self.template_name, context)


class UsersDetail(View):
    template_name = 'users/user_detail.html'

    def get(self, request, id: int) -> HttpResponse:
        user = get_object_or_404(
            UserProfileProxy.objects.get_user_detail(), pk=id
        )
        context = {'current_user': user}
        return render(request, self.template_name, context)


class UsersProfile(View):
    template_name = 'users/profile.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        form = users.forms.CustomUserChangeForm(instance=user)
        profile_form = users.forms.ProfileForm(instance=user.profile)
        context = {'form': form, 'profile_form': profile_form}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user

        form = users.forms.CustomUserChangeForm(request.POST, instance=user)
        profile_form = users.forms.ProfileForm(
            request.POST, request.FILES, instance=user.profile
        )

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()

        context = {'form': form, 'profile_form': profile_form}
        return render(request, self.template_name, context)


class UserRecovery(View):
    template_name = 'users/recovery.html'

    def get(self, request: HttpRequest, name: str) -> HttpResponse:
        user = get_object_or_404(User, username=name)
        if (
            user.profile.account_blocking_date is not None
            and user.profile.account_blocking_date
            > timezone.now() + timedelta(days=7)
            and not user.is_active
        ):
            user.delete()
            messages.error(request, 'User deleted')
        elif user.is_active is False:
            user.is_active = True
            user.profile.login_failed_count = 0
            user.profile.account_blocking_date = None
            user.profile.save()
            user.save()
            messages.success(request, 'Account restored!')
        else:
            messages.success(request, 'Account does not require recovery')

        return render(request, self.template_name)
