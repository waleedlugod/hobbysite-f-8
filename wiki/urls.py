from django.urls import path, include
from django.contrib import admin
from .views import article_list_view, article_detail_view

urlpatterns = [
    path("articles", article_list_view, name="article-list"),
    path("article/<int:pk>", article_detail_view, name="article-detail"),
]

app_name = "wiki"
