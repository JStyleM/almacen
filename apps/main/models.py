from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Almacen(models.Model):

	nombre = models.CharField(max_length=100)
	piso  = models.IntegerField()

	def __str__(self):
		return self.nombre + " - Piso " + str(self.piso)


class Denominacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class Remitente(models.Model):
	nombre = models.CharField(max_length=100)
		
	def __str__(self):
		return self.nombre


class Item(models.Model):
	nombre =  models.CharField(max_length=100)
	stock = models.IntegerField()
	denominacion = models.ForeignKey(Denominacion, on_delete=models.CASCADE)
	almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
   

class Movimientos(models.Model):

	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	fecha = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __str__(self):
		return self.item.nombre
