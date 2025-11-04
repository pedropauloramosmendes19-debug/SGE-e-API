from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from . import models
from . import forms
from . import serializer
from django.urls import reverse_lazy
from app import metrics
from category.models import Category
from brand.models import Brand
from rest_framework import generics


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = "product_list.html"
    context_object_name = 'products'
    permission_required = 'product.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        if category:
            queryset = queryset.filter(category_id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metrics()
        context['category'] = Category.objects.all()
        context['brand'] = Brand.objects.all()
        return context



class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = "product_detail.html"
    permission_required = 'product.view_product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForms
    template_name = "product_create.html"
    success_url = reverse_lazy('product_list')
    permission_required = 'product.create_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductForms
    template_name = "product_update.html"
    success_url = reverse_lazy('product_list')
    permission_required = 'product.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = "product_delete.html"
    success_url = reverse_lazy('product_list')
    permission_required = 'product.delete_product'


class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializers


