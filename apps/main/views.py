from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Item, Movimiento
from .forms import ItemForm, MovimientoForm


# Create your views here.

def home(request):	
	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})

def movimientos(request):	
	query = Movimiento.objects.all()
	return render(request, 'movimientos.html', {'query':query})

def item_update(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto','')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.cantidad = item.cantidad - int(cant)
			item.save()

		print(id_item)
		print(cant)	
	return redirect(reverse('main:movimientos'))

class CreateItem(CreateView):
	model = Item
	form_class = ItemForm
	template_name = 'create.html'
	success_url = reverse_lazy('main:home')

# class CreateMovimiento(CreateView):
# 	model = Movimiento
# 	form_class = MovimientoForm
# 	template_name = 'reg_movimiento.html'

# 	def get_success_url(self):

# 		item = Item.objects.get(nombre=self.object.item.nombre)
# 		item.stock = item.stock + self.object.cantidad
# 		item.save()
# 		return reverse_lazy('main:crear_movimiento')

def crear_movimiento(request):
	if request.method=="POST":

		form = MovimientoForm(request.POST)	
		print(request.POST['cantidad'])
		print(request.POST['item'])
		print(request.user)
		print(form)
		if form.is_valid():
			reg = form.save(commit=False)
			reg.tipo = 'Ingreso'
			reg.usuario = request.user
			reg.save()
			item = Item.objects.get(id=request.POST['item'])
			item.stock = item.stock + int(request.POST['cantidad'])
			item.save()
			return redirect('main:home')
	else:
		print("Formulario no valido")
		form = MovimientoForm()	
	return render(request, 'reg_movimiento.html', {'form': form})
