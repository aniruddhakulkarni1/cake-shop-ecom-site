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
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def chekout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        
    context = {'items':items,'order':order}
    return render(request, 'store/chekout.html', context)

def updateItem(request):
    data = json.loads(request.data)
    productID = data['productID']
    action = data['action']
    print("wrewtree")
    print('Action:',action)
    print('productId:',productID)
    return JsonResponse('Item was Added', safe=False)
    