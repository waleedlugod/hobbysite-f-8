from django.urls import path

from .views import product_list, product_detail, product_create, product_update, cart_list, transaction_list


urlpatterns = [
    path('items', product_list, name = 'list'),
    path('item/<int:pk>', product_detail, name = 'detail'),
    path("item/add", product_create, name = "product_create"),
    path("item/<int:pk>/edit", product_update, name = "product_edit"),
    path("cart", cart_list, name="cart"),
    path("transactions", transaction_list, name="transaction"),
]

app_name = "merchstore"