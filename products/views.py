from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product
from .forms import OrderingForm
# Create your views here.

def Home(request):
    return render(request , 'products/main.html')


def Products(request):
    product = Product.objects.all()
    name = None
    if 'searchname' in request.GET :
        name = request.GET['searchname']
        if name:
            product = product.filter(name__icontains=name)

    
    context={
        'product':product,
        'name':name
    }
    return render(request , 'products/products.html',context)


def ProductDetails(request,product_id):
    product = get_object_or_404(Product , id=product_id)
    context = {
        'product':product
    }
    return render(request , 'products/product_details.html',context)

def Ordering(request , product_id):
    product = get_object_or_404(Product , id=product_id)
    form = OrderingForm()
    if request.method == 'POST':
        form = OrderingForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request , 'The product has been ordered successfully')
            return redirect('main')
        else:
            OrderingForm()
    context = {
        'product':product,
        'form':form
    }
    return render(request , 'products/product_ordering.html',context)


