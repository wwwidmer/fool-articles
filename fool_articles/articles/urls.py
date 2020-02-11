from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article", views.ArticleView.as_view()),
]
