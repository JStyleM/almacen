from django.contrib import admin

from .models import Almacen, Denominacion, Target, Item, Movimiento

# Register your models here.

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'piso',)

@admin.register(Denominacion)
class DenominacionAdmin(admin.ModelAdmin):
	list_display = ('__str__',)

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
	list_display = ('__str__',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('__str__','stock','denominacion','almacen',)

# @admin.register(TipoMovimiento)
# class TipoMovimientoAdmin(admin.ModelAdmin):
# 	list_display = ('__str__',)

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
	list_display = ('__str__','tipo','cantidad','fecha','usuario',)



