from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializer
from rest_framework import generics


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'supplier'
    paginate_by = 6
    permission_required = 'supplier.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplier.create_supplier'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'supplier.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    template_name = 'supplier_update.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplier.change_supplier'




class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplier.delete_supplier'


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializer.SuppliersSerializers


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializer.SuppliersSerializers


