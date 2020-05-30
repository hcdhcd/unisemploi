from django.urls import path

from . import views
from django.shortcuts import render, redirect

urlpatterns = [
	path('', views.annuaire, name='annuaire'),
	path('detail_metier/<int:pk>', views.detailMetier, name='detailMetier'),
	path('add_file/<str:classe>/<int:pk>', views.add_file, name='add_file'),
	path('prendre_contact/<str:classe>/<int:pk>', views.prendre_contact, name='prendre_contact'),
	path('step0', views.step0, name='step0'),
	path('step1', views.step1, name='step1'),
	path('step2', views.step2, name='step2'),
	path('step3', views.step3, name='step3'),

]