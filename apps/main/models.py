from django.db import models

# Create your models here.

class Almacen(models.Model):

	nombre = models.CharField(max_length=100)
	piso  = models.IntegerField()

	def __str__(self):
		return self.nombre

class Denominacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class Item(models.Model):

	nombre = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	denominacion = models.ForeignKey(Denominacion, on_delete=models.CASCADE)
	almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
   