from django.contrib import admin
from django.urls import path
from .views import ContactView ,Home

urlpatterns = [
    path('',Home.as_view(),name='Home'),
    path('contact',ContactView.as_view(),name='contact'),
   
]