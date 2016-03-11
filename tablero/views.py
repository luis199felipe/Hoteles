#encoding:utf-8
from django.shortcuts import *
from django.template import loader,Context
from django.http import HttpResponseRedirect
from tablero.forms import loginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from tablero.models import Habitacion,Hotel

@login_required()
def home(request):
  hotel = Hotel.objects.filter(propietario=request.user)
  if len(hotel) == 1:
    habitaciones = Habitacion.objects.filter(hotel=hotel)
    print list(habitaciones.values())
    UnHotel = True
  else:
    habitaciones = {}

    UnHotel = False
    i=0
    for x in hotel:
       habitaciones[x.nombre] = Habitacion.objects.filter(hotel=x)
       i = i+1
    hotel = Hotel.objects.filter(propietario=request.user).values('id')
    habitaciones = habitaciones.items()

  return render(request,'inicio.html',{
    'usuario':request.user,
    'habitaciones':habitaciones,
    'UnHotel':UnHotel,
    'Hotel':hotel,
  })

@login_required()
def vistaPorHabitacion(request,idHabitacion,idHotel):
  hotel = Hotel.objects.get(id=idHotel)
  habitacion = Habitacion.objects.filter(id_habitacion=idHabitacion,hotel=hotel)
  return render(request,'vistaPorHabitacion.html',{
    'usuario':request.user,
    'habitacion':habitacion,
    'hotel':hotel,
    'idHabitacion':idHabitacion
    })

@login_required()
def vistaPerfil(request):
    user =request.user
    hoteles = Hotel.objects.filter(propietario=user)
    return render(request,'perfil.html',{
    'usuario':user,
    'hotel':hoteles
    })

def funcion(request,idHotel,idHabitacion,state):
   if state=='1':
      state = "Ocupado"
   else:
      state = "Libre"

   hotel = Hotel.objects.get(id=idHotel)
   new_estate = Habitacion(estado=state,id_habitacion=idHabitacion,hotel=hotel)
   new_estate.save()
   return render(request,'funcion.html',{'idHotel':idHotel,'idHabitacion':idHabitacion,'state':state})

def ingresar(request):
   if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password = password)
      if user is not None:
         if user.is_active:
            print "Usuario activo y autenticado"
            login(request, user)
            return HttpResponseRedirect('home')
         else:
            print "The password is valid, but the account has been disabled!"
      else:
         print "The username and password were incorrect."
   return render(request,'ingresar.html',{'datos':{'titulo':'Ingrese'},'form':loginForm})

def salir(request):
   logout(request)
   return redirect('/')
