from django.urls import path
from . import  views


urlpatterns = [
    path('supplier/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/supplier/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-retrieve-update-destroy'),
]