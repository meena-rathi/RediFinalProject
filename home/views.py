from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Image, CartItem
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index_view(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html')
def signout(request):
    return render(request, 'signout.html')


def gallery_view(request):
    photos = Image.objects.all()
    return render(request,"gallery.html", {"photos":photos})

def add_to_cart(request, product_id):
    product = get_object_or_404(Image, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # Implement adding to cart logic here
    # return render(request, 'cart.html')

    return redirect('cart_view')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.quantity > 1:
            # If quantity is greater than 1, decrement by 1 and save
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # If quantity is 1, remove the item from the cart
        cart_item.delete()
    
    return redirect('cart_view')
    # cart_item.delete()
    # return redirect('cart_view')

def cart_view(request):
    cart_items = CartItem.objects.all()
    for item in cart_items:
            item.total_price = item.quantity * item.product.price

    total_price = sum(item.total_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)
    # total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
def update_quantity(request, cart_item_id):
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        if request.method == 'POST':
             new_quantity = request.POST.get('quantity')
             cart_item.quantity = new_quantity
             cart_item.save()
        return HttpResponseRedirect(reverse('cart_view'))
        # return HttpResponseRedirect('/cart/')