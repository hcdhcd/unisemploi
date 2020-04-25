from django.urls import path

from . import views
from django.shortcuts import render, redirect

urlpatterns = [

	path('a_propos', views.apropos, name='apropos'),
	path('contact', views.contact, name='contact'),
	path('add_contact', views.add_contact, name='addContact'),
	
	

]