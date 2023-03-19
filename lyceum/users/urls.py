import django.contrib.auth.views
import django.urls

app_name = 'users'
urlpatterns = [
    django.urls.path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='users/login.html'
        ),
        name='login',
    ),
]
