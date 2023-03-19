from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.mail import send_mail

from users.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.conf import settings


class Register(View):
    template_name = 'users/register.html'

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
                    f'- « http://127.0.0.1:8000/auth/activate/{form.cleaned_data["username"]} »',
                    settings.MAIL_SENDER,
                    [f'{form.cleaned_data["email"]}'],
                    fail_silently=False,
                )

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('homepage:home')
        context = {'form': form}
        return render(request, self.template_name, context)
