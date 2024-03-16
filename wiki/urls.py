from django.urls import path, include
from django.contrib import admin
from .views import WikiListView, WikiDetailView

urlpatterns = [
    path("wiki/articles", WikiListView.as_view(), name="article-list"),
    path("wiki/article/<int:pk>", WikiDetailView.as_view(), name="article-detail"),
]

app_name = "wiki"
