from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms, serializer
from django.urls import reverse_lazy
from rest_framework import generics



class InflowListView(LoginRequiredMixin, PermissionRequiredMixin,   ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflow'
    paginate_by = 6
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    form_class = forms.InflowForms
    template_name = 'inflow_create.html'
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflow.create_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializer.InflowsSerializers
