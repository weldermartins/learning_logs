""" Define padrões de URL para users. """
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

app_name =  'users'
urlpatterns= [
	# Pagina de login
	url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
	

]
