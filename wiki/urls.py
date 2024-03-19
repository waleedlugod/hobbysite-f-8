from django.urls import path, include
from django.contrib import admin
from .views import article_list_view, article_detail_view

urlpatterns = [
    path("wiki/articles", article_list_view, name="article-list"),
    path("wiki/article/<int:pk>", article_detail_view, name="article-detail"),
]

app_name = "wiki"
