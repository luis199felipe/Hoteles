#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

#Crea los modelos Aquí
class Hotel(models.Model):
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	propietario = models.ForeignKey(User)


class Habitacion(models.Model):
	id_habitacion = models.IntegerField()
	estado = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now=True)
	hotel = models.ForeignKey(Hotel)


# Configuración de vista del administrador
class HotelAdmin(admin.ModelAdmin):
	list_display = ("id","nombre","direccion","propietario")
	fields = ["nombre","direccion","propietario"]

admin.site.register(Hotel)
admin.site.register(Habitacion)
