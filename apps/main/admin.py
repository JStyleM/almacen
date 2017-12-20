from django.contrib import admin

from .models import Almacen, Item

# Register your models here.

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'piso')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'almacen', 'cantidad', 'denominacion')


