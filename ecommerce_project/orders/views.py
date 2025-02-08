from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('product_list')

def view_cart(request):
    order = Order.objects.get(user=request.user, completed=False)
    return render(request, 'orders/view_cart.html', {'order': order})
