from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Cart
from orders.models import Product

# Create your views here.
def view(request):
    cart = Cart.objects.all()[0]
    context = {
        "cart": cart
    }
    return render(request, "carts/view.html", context)

def update_cart(requests, slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    
    return HttpResponseRedirect(reverse("cart"))



