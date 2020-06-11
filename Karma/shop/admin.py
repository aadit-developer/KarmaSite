from django.contrib import admin
from .models import Products,Order,OrderItem,Customer
# Register your models here.

admin.site.register(Products)
admin.site.register(Customer)
