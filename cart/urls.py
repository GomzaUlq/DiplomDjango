
from django.urls import path
from .views import add_to_cart, view_cart, update_cart_item, remove_from_cart, checkout

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('update_cart/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]
