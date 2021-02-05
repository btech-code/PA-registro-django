"""Define padrões de URL para users"""

from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'
urlpatterns = [
      # Página de login
      url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
      # Página de logout
      url(r'^logout/$', views.logout_view, name='logout'),
      # url(r'^logout/$', LogoutView.as_view(template_name='users/login.html'), name='logout'),
      # Página de cadastro
      url(r'^register/$', views.register, name='register'),
]