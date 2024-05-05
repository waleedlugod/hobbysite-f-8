from django.urls import include, path
from .views import blog_list_view, blog_detail_view, blog_update_view

urlpatterns = [
    path("article/<int:pk>", blog_detail_view, name="blog-detail"),
    path("articles", blog_list_view, name="blog-list"),
    path("article/<int:pk>/edit", blog_update_view, name="blog-update"),
]

app_name = "blog"
