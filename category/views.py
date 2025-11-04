from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from category.serializers import CategorySerializer


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'category'
    paginate_by = 6
    permission_required = 'category.view_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'category.add_view'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
    permission_required = 'category.view_category'

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'category.change_category'


class CategoryDeleteVieW(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'category.delete_category'


class CategoryCreateListAPIView(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


