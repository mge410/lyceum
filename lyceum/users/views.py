from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


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
        try:
            user = User.objects.get(username=name)
            if user.is_active is False:
                user.is_active = True
                user.save()
                messages.success(
                    request, 'KO!'
                )
            else:
                messages.success(
                    request, 'KO!!!'
                )
        except Exception:
            messages.error(
                request, 'User does not exist =('
            )
        return render(request, self.template_name, context)
