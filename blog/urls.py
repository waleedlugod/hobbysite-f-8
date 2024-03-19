from django.urls import include, path
from .views import blog_list_view, blog_detail_view

urlpatterns = [
    path("detail/<int:pk>", blog_detail_view, name="blog-detail"),
    path("list", blog_list_view, name="blog-list"),
]

app_name = "blog"
