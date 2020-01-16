from django.urls import path

from . import views
from django.shortcuts import render, redirect

urlpatterns = [
	path('', views.annuaire, name='annuaire'),
	path('a_propos', views.apropos, name='apropos'),
	path('contact', views.apropos, name='contact'),
	path('add_contact', views.add_contact, name='addContact'),


]