from django.urls import path

from .views import commission_create, commission_detail, commission_list, commission_edit

urlpatterns = [
    path("list", commission_list, name="commission_list"),
    path("detail/<int:pk>", commission_detail, name="commission_detail"),
    path("add", commission_create, name="commission_create"),
    path("<int:pk>/edit", commission_edit, name="commission_create"),
]

app_name = "ledger"
