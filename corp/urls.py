from django.urls import path
from . import views

urlpatterns = [
	# Lien du menu
	# Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/corp/
	path('', views.index, name='index'),
	# Lien pour s'inscrire au site
	# Pour y acceder changer l'url comme ceci http://127.0.0.1:8000/corp/register/
	path('register/', views.registerPage, name='register'),

	#page non fonctionnelle ; a revoir
	path('carousel/', views.carousel, name='caroussel'),

]
