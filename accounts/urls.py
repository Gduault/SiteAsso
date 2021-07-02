from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True,
                                                authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'),
         name='logout'),
    path('gestiondeprofil/<int:id_adh>', views.update_adherent, name='gestion'),
    # Change Password
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='accounts/changer.html',
                                                                   success_url='/'), name='change_password'),

]
