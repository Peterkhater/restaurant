from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
path('',views.main,name='restaurant'),
path('menu/',views.menu,name='menu'),
path('menuAEmporter/',views.menuEmporter,name='menuAEmporter')
]