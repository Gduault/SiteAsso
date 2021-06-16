from django.urls import path, include

from . import views

app_name = 'notif'
urlpatterns = [
    path('', views.notification, name='notification'),
]