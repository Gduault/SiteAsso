from django.urls import path

from . import views

app_name = 'evenement'
urlpatterns = [
    path('', views.afficheagenda, name='agenda'),
]