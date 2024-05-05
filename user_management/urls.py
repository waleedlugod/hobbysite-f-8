from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from .views import register_view, profile_index, profile_update

urlpatterns = [
    path("", profile_index, name="profile-index"),
    path("register/", register_view, name="register"),
    path("update/", profile_update, name="update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "user_management"
