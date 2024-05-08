from django.urls import path

from .views import profile_dashboard, profile_update, register_view

urlpatterns = [
    path("", profile_update, name="update"),
    path("dashboard/", profile_dashboard, name="dashboard"),
    path("register/", register_view, name="register"),
]

app_name = "user_management"
