from django.urls import include, path
from .views import blog_list, blog_detail

urlpatterns = [
    path("detail", blog_detail, name="blog-detail"),
    path("list", blog_list, name="blog-list"),
]

app_name = "blog"
