#encoding:utf-8
from django.conf.urls import *
from django.contrib import admin
from tablero.views import vistaPorHabitacion,home,vistaPerfil,salir,funcion,ingresar

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^home/',home,name='inicio'),
	url(r'^funcion/([0-9]{1})/([0-9]{3})/([0-9]{1})/$',funcion,name='funcion'),
	url(r'^$',ingresar,name='ingresar'),
	url(r'^perfil/',vistaPerfil,name='perfil'),
	url(r'^salir/',salir,name='salir'),
	url(r'^vistaPorHabitacion/([0-9]{3})/([0-9]{1})',vistaPorHabitacion),
]
