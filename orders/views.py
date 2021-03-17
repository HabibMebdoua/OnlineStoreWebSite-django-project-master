from django.shortcuts import render
from products.models import Order
from django.views.generic import DeleteView
# Create your views here.

def all_orders(request):
    orders = Order.objects.all()

    context={
        'orders':orders
    }

    return render(request , 'orders/all_orders.html' , context)

class OrderDone(DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    pk_url_kwarg = 'order_id'
    context_object_name = 'order'
    success_url = '/'
