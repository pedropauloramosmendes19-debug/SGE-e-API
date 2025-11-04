from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms, serializer
from django.urls import reverse_lazy
from app.metrics import get_sales_metrics
from rest_framework import generics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflows
    template_name = 'outflows_list.html'
    context_object_name = 'outflow'
    paginate_by = 6
    permission_required = 'outflows.view_outflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sales_metrics'] = get_sales_metrics()
        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflows
    form_class = forms.OutflowForms
    template_name = 'outflows_create.html'
    success_url = reverse_lazy('outflows_list')
    permission_required = 'outflow.create_outflow'

class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outflows
    template_name = 'outflows_detail.html'
    permission_required = 'outflows.view_outflows'

class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflows.objects.all()
    serializer_class = serializer.OutflowSerializer
