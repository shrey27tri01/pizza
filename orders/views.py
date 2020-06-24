from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from .forms import RegistrationForm
from .models import Pizza, Toppings, Subs, DinnerPlatters, Pasta, Salads, Product

# Create your views here.
def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, "orders/login.html", {"messsage": None})

              
        return HttpResponse("Item added to cart")

    else:
        if not request.user.is_authenticated:
            return render(request, "orders/login.html", {"messsage": None})
        
        context = {
            "user": request.user,   
            "pizzas": Pizza.objects.all(),
            "toppings": Toppings.objects.all(),
            "subs": Subs.objects.all(),
            "dinnerplatters": DinnerPlatters.objects.all(),
            "pasta": Pasta.objects.all(),
            "salads": Salads.objects.all()
        }
        return render(request, "orders/dashboard.html", context)

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "orders/login.html", {"message": "Invalid Credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    form = RegistrationForm()
    context = {
        "form": form,
        
    }
    return render(request, "orders/signup.html", context)  



'''
def cart(request, user_name):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"messsage": None})

    context = {
        "user": request.user
    }
    return render(request, "orders/cart.html", context)
'''


'''
def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders
    } 
    return render(request, "profile.html", context)

def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('id', "")).first()
    if product in request.user.profile.items.all():
        #messages.info(request, 'You already own this item')
        return HttpResponseRedirect(reverse('dashboard'))
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
     
    return HttpResponseRedirect(reverse('dashboard'))
'''