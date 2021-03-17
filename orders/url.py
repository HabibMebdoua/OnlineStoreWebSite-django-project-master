from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_orders, name='all'),
    path('order_done/<int:order_id>', views.OrderDone.as_view(), name='order_done'),
]
