from django.urls import path

from .views import merch_list_view, merch_detail_view


urlpatterns = [
    path('items', merch_list_view, name = 'list'),
    path('item/<int:pk>', merch_detail_view, name = 'detail')
]

app_name = "merchstore"