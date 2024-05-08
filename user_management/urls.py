from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import register_view, profile_dashboard, profile_update

urlpatterns = [
    path("", profile_update, name="update"),
    path("dashboard/", profile_dashboard, name="dashboard"),
    path("register/", register_view, name="register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "user_management"
