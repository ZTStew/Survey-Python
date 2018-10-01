from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('results', views.results),
    path('back', views.back),
]