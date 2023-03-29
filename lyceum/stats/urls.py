import stats.views
from django.urls import path

app_name = 'userstats'
urlpatterns = [
    path(
        '<int:id>',
        stats.views.UserStatsView.as_view(),
        name='userstatsview',
    ),
]
