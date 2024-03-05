from django.urls import path

from .views import commission_list

urlpatterns = [
    path("list", commission_list, name="commission_list"),
]

app_name = "ledger"
