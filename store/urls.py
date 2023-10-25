from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('category/<int:pk>', views.get_all_products),
    path('product/<int:product_id>', views.product_detail),
    path('add-to-cart/<int:product_id>', views.add_to_cart),
    path('my-cart/', views.user_cart),
    path('about/', views.about),
    path('contacts/', views.contact),
    path('del-item/<int:cart_id>', views.del_item),
]