from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('nombre', 'cantidad', 'denominacion', 'almacen')
		widgets = {
			'nombre' : forms.TextInput(attrs={
				'type' : 'text',
				'placeholder' : 'Nombre',
				'class' : 'form-control'
				}),
			'cantidad' : forms.TextInput(attrs={
				'type' : 'number',
				'placeholder' : '0',
				'class' : 'form-control'
				}),
			'denominacion' : forms.Select(attrs={
				'class' : 'form-control'
				}),
			'almacen' : forms.Select(attrs={
				'class' : 'form-control'
				})
		}

	

