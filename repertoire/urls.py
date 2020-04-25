from django.urls import path

from . import views
from django.shortcuts import render, redirect

urlpatterns = [
	path('', views.annuaire, name='annuaire'),
	path('detail_metier/<int:pk>', views.detailMetier, name='detailMetier'),
	path('add_file/<str:classe>/<int:pk>', views.add_file, name='add_file'),
	path('prendre_contact/<str:classe>/<int:pk>', views.prendre_contact, name='prendre_contact'),


]