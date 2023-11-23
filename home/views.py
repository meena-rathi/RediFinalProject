from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Image, CartItem
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html')

# See all the product in gallery.html
def gallery_view(request):
    photos = Image.objects.all()
    return render(request,"gallery.html", {"photos":photos})

# add the product  into cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Image, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        if product.available_quantity > 0:
            cart_item.quantity += 1
            cart_item.save()
            product.available_quantity -= 1
            product.save()
        else:
            messages.warning(request, 'Product out of stock')
    else:
        if product.available_quantity > 0:
            product.available_quantity -= 1
            product.save()
    return redirect('cart_view')

# remove the item from cart or remove the quantity form cart
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    product = cart_item.product
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
    return redirect('cart_view')

#    Cart view shows the number of item add
def cart_view(request):
    cart_items = CartItem.objects.all()
    for item in cart_items:
            item.total_price = item.quantity * item.product.price

    total_price = sum(item.total_price for item in cart_items)
    quantity_range = list(range(1, 5))  

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'quantity_range': quantity_range,
    }
    return render(request, 'cart.html', context)

    # Update the quantity in cart
def update_quantity(request, cart_item_id):
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        if request.method == 'POST':
            new_quantity = request.POST.get('quantity')
        old_quantity = cart_item.quantity
        cart_item.quantity = new_quantity
        cart_item.save()
        new_quantity = int(new_quantity)
        old_quantity = int(old_quantity)
        product = cart_item.product
        if int(new_quantity) < int(old_quantity):
            product.available_quantity += old_quantity - new_quantity
        else:
            product.available_quantity -= new_quantity - old_quantity
        product.save()
        return HttpResponseRedirect(reverse('cart_view'))

    #  contact form
def contact_view(request):
    if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('success_view') 
    else:
          form = ContactForm
          return render(request, 'contact_form.html', {'form': form})
    
# contact form redirecting to succes.html
def success_view(request):
    return render(request, 'success.html')

