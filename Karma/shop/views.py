from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Customer,Products,Order,OrderItem
from django.http import JsonResponse
import json
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
username=''
check=True
def login(request):
    if request.method=="GET":
        
        return render(request,'login.html')

    else:
        global username
        username = request.POST['username']
        password=request.POST['password']
        try:
            user=Customer.objects.get(username=username,password=password)
            products=Products.objects.all()
        

            if user is not None:
                return render(request,'index.html',{'products':products})
        except :
            messages.info(request,'Wrong Credentials')
            return render(request,'login.html')


def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    
    else:
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        name=request.POST['name']
        if(username=='' or password=='' or email=='' or name==''):
            messages.info(request,'All details are necessary')
            return render(request,'register.html')
        user=Customer(name=name,email=email,username=username,password=password)
        user.save()
        return render(request,'login.html')
    

def updateOrder(request):
    data=json.loads(request.body)
    product_Id=data['productId']
    action=data['action']
    global check
    customer=Customer.objects.filter(username=username)
    product=Products.objects.get(id=product_Id)
    order,created=Order.objects.get_or_create(customer=customer[0],complete=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order,product=product)
    if action=="add":

        orderItem.quantity=(orderItem.quantity + 1)

        if (orderItem.quantity>product.product_stock):
            check=False
        
    elif action=="remove":
        orderItem.quantity=(orderItem.quantity - 1)
        if (orderItem.quantity>product.product_stock):
            check=False
    
    orderItem.save()
    return JsonResponse('item was added',safe=False)

def cart(request):
    customer=Customer.objects.filter(username=username)
    order,created = Order.objects.get_or_create(customer=customer[0],complete=False)
    items= order.orderitem_set.all()
    return render(request,'cart.html',{'items':items,'order':order})

def home(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})

def search(request):
    query=request.POST['search']
    print(query)
    product=Products.objects.get(product_name=query)
    return render(request,'index.html',{'products':product})

def checkout(request):
    global check
    if(check==False):
        customer=Customer.objects.filter(username=username)
        cust=Customer.objects.get(username=username)
        order,created = Order.objects.get_or_create(customer=customer[0],complete=False)
        items= order.orderitem_set.all()
        check=True
        email_subject='Order was failed to place'
        email_message = EmailMessage(
                            email_subject,
                            'Sorry but you have selected out of stock quantities!Please reselect the quantities and try again!',
                            settings.EMAIL_HOST_USER,
                            [cust.email]

        )
        email_message.send()
        return redirect('cart')
    else:
        cust=Customer.objects.get(username=username)
        products=Products.objects.all()
        email_subject='Order placed Successfully'
        email_message = EmailMessage(
                            email_subject,
                            'Your order has been placed successfully! Thank you for shopping with us!',
                            settings.EMAIL_HOST_USER,
                            [cust.email]

        )
        email_message.send()
        return render(request,'index.html',{'products':products})