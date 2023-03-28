import about.urls
import catalog.urls
import django.contrib.admin
import django.contrib.auth.urls
import django.urls
import download.urls
import feedback.urls
import homepage.urls
import users.urls
import statistic.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    django.urls.path('', django.urls.include(homepage.urls)),
    django.urls.path('about/', django.urls.include(about.urls)),
    django.urls.path('feedback/', django.urls.include(feedback.urls)),
    django.urls.path('catalog/', django.urls.include(catalog.urls)),
    django.urls.path('download/', django.urls.include(download.urls)),
    django.urls.path('statistic/', django.urls.include(statistic.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('auth/', django.urls.include(users.urls)),
    django.urls.path('auth/', django.urls.include(django.contrib.auth.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    import debug_toolbar

    urlpatterns.append(
        django.urls.path('__debug__/', django.urls.include(debug_toolbar.urls))
    )
