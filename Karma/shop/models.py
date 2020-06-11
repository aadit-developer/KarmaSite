from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField()
    product_price=models.IntegerField()
    product_stock=models.IntegerField()

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)

    @property
    def get_cart_total(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        total=total + total * (0.18)
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.product_price * self.quantity
        return total