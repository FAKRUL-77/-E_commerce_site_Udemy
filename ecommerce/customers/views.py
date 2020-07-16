from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm, CustomerLoginForm
from .models import Customer

# Create your views here.
from django.views.generic import CreateView


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer/customer_signup_form.html'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        customer = Customer.objects.create(user=user)

        customer.phone = form.cleaned_data.get('phone')
        customer.dob = form.cleaned_data.get('dob')
        customer.gender = form.cleaned_data.get('gender')

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        customer.name = first_name+" "+last_name

        customer.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('home')


class CustomerLoginView(SuccessMessageMixin, LoginView):
    form_class = CustomerLoginForm
    redirect_authenticated_user = True
    template_name = 'customer/login_form.html'
    success_message = 'You are successfully logged in'


class CustomerLogoutView(LogoutView):
    next_page = 'home'


def home(request):
    return render(request, 'home_page.html')
