# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from models import *

# Create your views here.


def index(request):
    items= Item.objects.all()
    context = {
        'category': Item.objects.values('category').distinct().annotate(count=Count('category')),
        'items': items,
    }
    return render(request, 'ecommerce/home.html', context)

def search(request):
    items=Item.objects.filter(name__startswith=request.POST['search'])

    return render(request, 'ecommerce/all_items.html', {"items": items})

def searchcat(request):
    items=Item.objects.filter(category=request.POST['category'])
    return render(request, 'ecommerce/all_items.html', {'items': items, 'category': request.POST['category']})

def sortby(request):
    items=Item.objects.all.order_by(request.POST['sorted'])
    return render(request, 'ecommerce/all_items.html', {'items': items})

def all_items(request):
    items= Item.objects.all()
    context = {
        'category': Item.objects.values('category').distinct().annotate(count=Count('category')),
        'items': items,
    }
    return render(request, 'all_items.html', context)

def item(request, item_id):
    context = {
        'all_burritos': Item.objects.filter(category="Burrito"), # need to pass in category......
        'item': Item.objects.get(id=item_id)
    }
    return render(request, 'ecommerce/item.html', context)

def addcart(request):
    if 'user' not in request.session:
        Cart.objects.create()
        request.session['user'] = Cart.objects.last()
    item = Item.objects.get(id=request.POST['item_id'])
    print request.POST['quantity_added']
    cart = Cart.objects.last()
    x = 1
    while (x <= int(request.POST['quantity_added'])):
         cart.items.add(item)

def admin(request):
    return render(request, 'ecommerce/index.html')

def login(request):
    if request.method == "POST":
        errors = User.objects.basic_login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
                return redirect('/')
        else:
            user = User.objects.get(email = request.POST['email'])
            if not 'admin' in request.session:
                request.session['admin'] = adminuser.id
    return redirect('/orders')

def orders(request):
    items = Cart.objects.all()
    return render(request, 'ecommerce/orders.html', {'orders': items})

def products(request):
    items = Item.objects.all()
    return render(request, 'ecommerce/products.html', {'product': items})

def logout(request):
    del request.session['admin']
    return redirect('/')



    #
    # cart.quantity = cart.quantity - int(request.POST['quantity_added'])
    # cart.save()
    # if "carts" not in request.session:
    #     request.session['carts'] = Cart.objects.create(
    #     id = request.session['user'],
    #     items = cart.id
    #     )
    # c = Cart.objects.last()
    # c.quantity_purchased = request.POST['quantity_added']

        #add to the cart if made

    return redirect('/main')



# Create shopping page
# View all items page with categories and search
# Specific Item Page to buy
# Checkout page with shipping and billing form/ with price and items in shopping cart
# --ADMIN
# -Orders
# Search thru Orders
# View All Orders with seperate pages for items
# Specifc order page with items and status
# --Products
# View all products and add new products
# Edit product popup
  # {% for item in items %}
  # <img src="static/ecommerce/img/{{item.image}}" alt="">
  # {% endfor %}
