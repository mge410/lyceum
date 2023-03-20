from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from users.forms import UserCreationForm
from users.models import Profile


class Register(View):
    template_name = 'users/signup.html'

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = settings.DEFAULT_USER_ACTIVITY
            user.save()
            profile = Profile(user=user)
            profile.save()

            if not settings.DEFAULT_USER_ACTIVITY:
                send_mail(
                    'Email verification',
                    f'Thank you for registering on our website! <br>'
                    f'Profile activation link! <br>'
                    f'- « http://127.0.0.1:8000/auth/activate/'
                    f'{form.cleaned_data["username"]} »',
                    settings.MAIL_SENDER,
                    [f'{form.cleaned_data["email"]}'],
                    fail_silently=False,
                )

            return redirect('homepage:home')
        context = {'form': form}
        return render(request, self.template_name, context)


class ActivateUsers(View):
    template_name = 'users/activate.html'

    def get(self, request, name):
        context = {}

        user = get_object_or_404(User, username=name)
        if (
            user.date_joined < timezone.now() - timedelta(hours=12)
            and user.is_active is False
        ):
            user.delete()
            messages.error(request, 'Activation expired =(')
        elif user.is_active is False:
            user.is_active = True
            user.save()
            messages.success(request, 'Activation was successful!')
        else:
            messages.success(request, 'User already activated!!!')

        return render(request, self.template_name, context)


class UsersList(View):
    template_name = 'users/user_list.html'

    def get(self, request):
        users = User.objects.filter(is_active=True)

        context = {
        }
        return render(request, self.template_name, context)
