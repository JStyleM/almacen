from django.contrib import admin

from .models import Almacen, Item

# Register your models here.

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'piso')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'almacen_name', 'cantidad', 'denominacion')


