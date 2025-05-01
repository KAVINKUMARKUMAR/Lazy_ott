from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
from .form import CustomLogin,CustomRegister
from django.contrib.auth.views import LoginView

class userregister(CreateView):
    form_class = CustomRegister
    template_name = 'signup.html'
    success_url = reverse_lazy('signin')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home or another page
        return super().dispatch(request, *args, **kwargs)

class userlogin(LoginView):
    form_class = CustomLogin
    template_name  = 'signin.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to the home page or any page you prefer
        return super().dispatch(request, *args, **kwargs)

