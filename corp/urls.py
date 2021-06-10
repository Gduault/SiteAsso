from django.urls import path
from . import views

urlpattern = [
	path('corp/',views.index, name='index'),
]
