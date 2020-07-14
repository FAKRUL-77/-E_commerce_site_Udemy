from django.urls import path, include
from .views import *
from .import views

urlpatterns = [
    path('customerSignUp/', StudentSignUpView.as_view(), name='register'),
    path('customerLogout/', CustomerLogoutView  .as_view(), name='logout'),
    path('', views.home, name='home'),
]