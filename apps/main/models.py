from django.db import models

# Create your models here.

class Almacen(models.Model):

	nombre = models.CharField(max_length=100)
	piso  = models.IntegerField()

	def __unicode__(self):
		return self.nombre


class Item(models.Model):

	nombre = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	denominacion = models.CharField(max_length=100)
	almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.nombre

	def almacen_name(self):
		return self.almacen.nombre