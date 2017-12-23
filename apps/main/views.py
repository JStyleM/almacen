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


def item_add(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto','')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.stock = item.stock + int(cant)
			item.save()
			cant = int(cant)
			obj = Movimiento(item=item, tipo='Ingreso', cantidad=cant, usuario=request.user)
			obj.save()
		print(id_item)
		print(cant)	
	return redirect(reverse('main:home'))

def item_retiro(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto','')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.stock = item.stock - int(cant)
			item.save()
			cant = int(cant)*(-1)
			obj = Movimiento(item=item, tipo='Retiro', cantidad=cant, usuario=request.user)
			obj.save()
		print(id_item)
		print(cant)	
	return redirect(reverse('main:home'))

def crear_item(request):
	if request.method=="POST":
		form = ItemForm(request.POST)
		print(form)
		if form.is_valid():
			reg = form.save(commit=False)
			reg.save()
			item_x = Item.objects.get(nombre=request.POST['nombre'])
			print(request.POST['nombre'])
			mov = Movimiento(item=item_x, tipo='Ingreso', cantidad=reg.stock, usuario=request.user, target=reg.target)
			mov.save()
			return redirect('main:home')
	else:
		print("Formulario no valido")
		form = ItemForm()

	return render(request, 'create.html', {'form': form})


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
