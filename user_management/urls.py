from django.urls import include, path
from .views import register_view

urlpatterns = [
    path("", register_view, name="update-profile"),
]

app_name = "user_management"
