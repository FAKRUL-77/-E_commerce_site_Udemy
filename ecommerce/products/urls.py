from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('featured/', ProductFeaturedListView.as_view(), name='product_featured_list'),
    path('featured/<str:pk>', ProductFeaturedDetailView.as_view(), name='product_featured_detail'),
    path('featured_slug/<str:slug>', ProductDetailSlugView.as_view(), name='product_slug_view'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<str:pk>', ProductDetailView.as_view(), name='product_detail'),
    # path('product/<str:slug>', ProductDetailView.as_view(), name='product_slug'),
    path('product-fbv/<str:pk>', product_detail_view, name='product_detail_fbv'),
]
