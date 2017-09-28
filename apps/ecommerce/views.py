# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.
def index(request):

    return redirect('/main')

def main(request):
    context = {
        'category': Item.objects.values('category').distinct().annotate(count=Count('category')),
        'items': Item.objects.all(),
    }
    return render(request, 'ecommerce/all_items.html', context)

def item(request, item_id):
    context = {
        'all_burritos': Item.objects.filter(category="Burrito"),
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
