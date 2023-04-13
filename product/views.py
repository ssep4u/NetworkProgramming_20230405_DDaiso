from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from product.models import Product


class ProductListView(ListView):
    model = Product
    # 'product_list.html', {'product_list': Product.objects.all()}


class ProductDetailView(DetailView):
    model = Product
    # 'product_detail.html', {'product': Product.objects.get(pk=pk)}


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']  # '__all__'
    template_name_suffix = '_create'  # product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')  #추가 성공하면, 이동할 url 이름
