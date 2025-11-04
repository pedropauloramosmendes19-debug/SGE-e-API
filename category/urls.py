from django.urls import path
from . import views


urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(),name='category_create'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteVieW.as_view(), name='category_delete'),

    path('api/v1/categories/', views.CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('api/v1/category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
]