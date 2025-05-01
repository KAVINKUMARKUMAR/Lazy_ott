from django.urls import path
from .views import userregister,userlogin

from django.contrib.auth import views

urlpatterns = [
     path('login/',userlogin.as_view(),name='signin'),
     path('register/',userregister.as_view(),name='signup'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
]

