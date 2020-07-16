from django.urls import path, include
from .views import *
from .import views

urlpatterns = [
    path('customerSignUp/', CustomerSignUpView.as_view(), name='register'),
    path('customerLogin/', CustomerLoginView.as_view(), name='login'),
    path('customerLogout/', CustomerLogoutView  .as_view(), name='logout'),
    path('', views.home, name='home'),
]