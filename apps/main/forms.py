from django import forms
from .models import Item, Movimiento

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('nombre', 'stock', 'denominacion', 'target', 'almacen')
		widgets = {
			'nombre' : forms.TextInput(attrs={
				'type' : 'text',
				'placeholder' : 'Nombre',
				'class' : 'form-control'
				}),
			'stock' : forms.TextInput(attrs={
				'type' : 'number',
				'value' : 0,
				'placeholder' : '0',
				'class' : 'form-control'
				}),
			'denominacion' : forms.Select(attrs={
				'class' : 'form-control'
				}),
			'target' : forms.Select(attrs={
				'class' : 'form-control'
				}),
			'almacen' : forms.Select(attrs={
				'class' : 'form-control'
				})
		}

	
class MovimientoForm(forms.ModelForm):

	class Meta:
		model = Movimiento
		fields = ('item', 'cantidad')
		widgets = {
			'item' : forms.Select(attrs={
				'class' : 'form-control'
				}),
			'cantidad' : forms.TextInput(attrs={
				'type' : 'number',
				'class' : 'form-control'
				}),
			'target' : forms.Select(attrs={
				'class' : 'form-control'
				}),

		}
