from django.urls import path

from .views import(
    index,
    AnimeListView
)

urlpatterns = [
    path("", index , name="index"),
    path("animes/", AnimeListView.as_view(), name= "anime_list")
]

app_name = "app_anime_list"