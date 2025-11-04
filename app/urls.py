from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),

    path('api/v1/', include('authentication.urls')),

    path('', include('brand.urls')),
    path('', include('category.urls')),
    path('', include('supplier.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('product.urls')),
]
