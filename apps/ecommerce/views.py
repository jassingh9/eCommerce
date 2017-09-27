# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.
def index(request):
    context= {
     "items": Item.objects.all()
    }
    return render(request, 'ecommerce/index.html', context)

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
