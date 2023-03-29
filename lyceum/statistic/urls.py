import statistic.views
from django.urls import path

app_name = 'userstats'
urlpatterns = [
    path(
        '<int:id>',
        statistic.views.UserStatsView.as_view(),
        name='userstatsview',
    ),
]
