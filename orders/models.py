from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save


User = get_user_model()

# Create your models here.
class Product(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = []




class Pizza(Product):
    pizzatype = models.CharField(max_length=15)
    extras = models.TextField(max_length=50)
    size = models.CharField(max_length=10)
    product_ptr = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True, primary_key=True, default=None)

    class Meta:
        verbose_name_plural = "Pizzas"

    def __str__(self):
        self.output =  f"{self.size} {self.pizzatype} pizza with {self.extras} costing {self.price} dollars"
        return self.output
    

class Toppings(models.Model):
    topping = models.TextField(max_length=64)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        self.output = f"Topping: {self.topping}"
        return self.output

class Subs(Product):
    name = models.TextField(max_length=64)
    size = models.CharField(max_length=10)
    product_ptr = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True, primary_key=True, default = None)


    class Meta:
        verbose_name_plural = "Subs"

    def __str__(self):
        self.output = f"{self.size} sub: {self.name} costing {self.price} dollars"
        return self.output

class DinnerPlatters(Product):
    name = models.TextField(max_length=64)
    size = models.CharField(max_length=10)
    product_ptr = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True, primary_key=True, default = None)


    class Meta:
        verbose_name_plural = "DinnerPlatters"

    def __str__(self):
        self.output = f"{self.size} Dinner Platter: {self.name} costing {self.price} dollars"
        return self.output

class Pasta(Product):
    name = models.TextField(max_length=64)
    product_ptr = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True, primary_key=True, default = None)


    class Meta:
        verbose_name_plural = "Pasta"

    def __str__(self):
        self.output = f"{self.name} pasta costing {self.price} dollars"
        return self.output

class Salads(Product):
    name = models.TextField(max_length=64)
    product_ptr = models.OneToOneField(Product, on_delete=models.CASCADE, parent_link=True, primary_key=True, default = None)


    class Meta:
        verbose_name_plural = "Salads"

    def __str__(self):
        self.output = f"{self.name} costing {self.price} dollars"
        return self.output


'''
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"Cart for user {self.user} created on {self.created_at}" 


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        self.output = f"{self.cart} - {self.product}" 
        return self.output
'''

'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user.username}"

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.product.price}"

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return f"{self.owner} - {self.ref_code}"

'''
