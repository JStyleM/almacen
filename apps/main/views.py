from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, View
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Item, Movimiento
from .forms import ItemForm, MovimientoForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):	
	query = Item.objects.order_by('-fecha')
	return render(request, 'index.html', {'query':query})

@login_required
def movimientos(request):	
	query = Movimiento.objects.order_by('-fecha')
	return render(request, 'movimientos.html', {'query':query})

class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url = reverse_lazy('main:home')

	def form_valid(self, form):
		print('is_valid')
		user = authenticate(
			username = form.cleaned_data['username'],
			password = form.cleaned_data['password']
			)
		login(self.request, user)
		return super(LoginView, self).form_valid(form)


class LogoutView(View):

	def get(self, request, *agrs, **kwargs):
		logout(request)
		return redirect(reverse('main:login'))

@login_required
def item_add(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto','')
		dest = request.GET.get('target','')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.stock = item.stock + int(cant)
			item.save()
			cant = int(cant)
			obj = Movimiento(item=item, tipo='Ingreso', cantidad=cant, usuario=request.user, target=dest)
			obj.save()
		print(id_item)
		print(cant)	
	return redirect(reverse('main:home'))

@login_required
def item_retiro(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto','')
		dest = request.GET.get('target','')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.stock = item.stock - int(cant)
			item.save()
			cant = int(cant)*(-1)
			obj = Movimiento(item=item, tipo='Retiro', cantidad=cant, usuario=request.user, target=dest)
			obj.save()
		print(id_item)
		print(cant)	
	return redirect(reverse('main:home'))

@login_required
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

@login_required
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
