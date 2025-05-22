from django.urls import path

from statistic import views

app_name = "statistic"
urlpatterns = [
    path(
        "chosen/",
        views.UserItemListView.as_view(),
        name="user_item_list",
    ),
    path(
        "<int:id>",
        views.UserStatisticView.as_view(),
        name="user_detail_statistics",
    ),
]
