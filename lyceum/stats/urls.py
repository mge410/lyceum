from django.urls import path

from .views import UserStatsView

app_name = 'userstats'
urlpatterns = [
    path(
        '<int:id>',
        UserStatsView.as_view(),
        name='userstatsview',
    ),
]
