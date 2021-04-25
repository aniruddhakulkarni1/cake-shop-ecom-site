from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import SignUpForm
from django.http import JsonResponse
import json
from .models import *


# Create your views here.

def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("SignUpDone")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})


def SignUpDone(request):
    return HttpResponse("Acoount Creaeted.!")



def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        item = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items= []
        order= {'get_cart_total':0, 'get_cart_items':0}
        cartItems= order['get_cart_items']
        products = Product.objects.all()
    
    context = {'products':products, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems= order['get_cart_items']
        products = Product.objects.all()
        
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems= order['get_cart_items']
        products = Product.objects.all()
        
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/chekout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("wrewtree")
    print('Action:',action)
    print('productId:',productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    Orderitem, created=Orderitem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        Orderitem.quantity = (Orderitem.quantity + 1)
    elif action == 'remove':
        Orderitem.quantity = (Orderitem.quantity - 1)
        Orderitem.save()

    if Orderitem.quantity <= 0:
        Orderitem.delete()
    
    return JsonResponse('Item was Added', safe=False)