from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article", views.ArticleView.as_view()),
    path("article/<uuid>/",
         views.ArticleView.as_view(), name="article-detail"
         ),
    path("article/<uuid>/comments", views.CommentListView.as_view()),
    path("article/<uuid>/comments/", views.CommentView.as_view()),
]
