from django.urls import include, path
from .views import register_view, profile_index, profile_update

urlpatterns = [
    path("", profile_index, name="profile-index"),
    path("register/", register_view, name="register"),
    path("update/", profile_update, name="update"),
]

app_name = "user_management"
