from django.urls import include, path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("detail/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("list", BlogListView.as_view(), name="blog-list"),
]

app_name = "blog"
