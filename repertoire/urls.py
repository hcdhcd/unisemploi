from django.urls import path

from . import views
from django.shortcuts import render, redirect

urlpatterns = [
	path('', views.annuaire, name='annuaire'),


]