from django.urls import path, include
from django.contrib import admin
from .views import (
    article_list_view,
    article_detail_view,
    article_update_view,
    article_create_view,
)

urlpatterns = [
    path("articles", article_list_view, name="article-list"),
    path("article/<int:pk>", article_detail_view, name="article-detail"),
    path("article/<int:pk>/edit", article_update_view, name="article-update"),
    path("article/add", article_create_view, name="article-create"),
]

app_name = "wiki"
