from statistic import views

from django.urls import path

app_name = 'statistic'
urlpatterns = [
    path(
        'chosen/',
        views.UserItemListView.as_view(),
        name='user_item_list',
    ),
]
