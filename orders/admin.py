from django.contrib import admin
from .models import Pizza, Toppings, Subs, DinnerPlatters, Pasta, Salads, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(DinnerPlatters)
admin.site.register(Pasta)
admin.site.register(Salads)

