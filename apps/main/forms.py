from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('nombre', 'cantidad', 'denominacion', 'almacen')
		widgets = {
			'nombre' : forms.TextInput(attrs={
				'type' : 'text',
				'placeholder' : 'Username'
				}),
			'cantidad' : forms.TextInput(attrs={
				'type' : 'email',
				'placeholder' : 'Email'
				}),
			'denominacion' : forms.Select(),
			'get_almacen' : forms.Select()
		}

	

