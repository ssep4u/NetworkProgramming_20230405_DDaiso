from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductListView(ListView):
    model = Product
    # 'product_list.html', {'product_list': Product.objects.all()}


class ProductDetailView(DetailView):
    model = Product
    # 'product_detail.html', {'product': Product.objects.get(pk=pk)}
