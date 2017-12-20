from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Item
from .forms import ItemForm


# Create your views here.

def home(request):	
	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})

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
	return redirect(reverse('main:home'))

class CreateItem(CreateView):
	model = Item
	form_class = ItemForm
	template_name = 'create.html'
	sucess_url = reverse_lazy('main:home')
