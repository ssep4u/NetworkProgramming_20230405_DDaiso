from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    model = Product
