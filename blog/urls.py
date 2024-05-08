from django.urls import include, path
from .views import (
    blog_list_view,
    blog_detail_view,
    blog_create_view,
    blog_update_view,
    blog_upload_gallery_images_view,
)

urlpatterns = [
    path("article/<int:pk>", blog_detail_view, name="blog-detail"),
    path("articles", blog_list_view, name="blog-list"),
    path("article/add", blog_create_view, name="blog-create"),
    path("article/<int:pk>/edit", blog_update_view, name="blog-update"),
    path(
        "article/<int:pk>/add_images",
        blog_upload_gallery_images_view,
        name="blog-upload-images",
    ),
]

app_name = "blog"
