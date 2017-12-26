from django import forms
from .models import Item, Movimiento
from django.contrib.auth.models import User

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
			'target' : forms.TextInput(attrs={
				'type' : 'text',
				'placeholder' : 'Nombre',
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

class LoginForm(forms.Form):
	
	username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
		'type' : 'text',
		'placeholder' : 'Usuario',	
		'class' : 'form-control',
		}))
	password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
		'type' : 'password',
		'placeholder' : 'Contraseña',
		'class' : 'form-control',
		}))

	def clean(self):
		user_found = User.objects.filter(username=self.cleaned_data['username']).exists()
		if not user_found:
			self.add_error('username', 'Usuario no encontrado')
		else:
			user = User.objects.get(username=self.cleaned_data['username'])
			if not user.check_password(self.cleaned_data['password']):
				self.add_error('password', 'Contraseña no coincide')

		print(self.cleaned_data)
