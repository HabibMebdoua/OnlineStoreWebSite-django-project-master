from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='main'),
    path('products', views.Products, name='products'),
    path('products/<int:product_id>', views.ProductDetails, name='product_details'),
    path('order/<int:product_id>', views.Ordering , name='product_ordering'),
]
