from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Item


# Create your views here.

def home(request):
	if request.method == 'GET':
		id_item = request.GET.get('item_id','')
		cant = request.GET.get('monto')
		if id_item != '':
			item = Item.objects.get(id=id_item)
			item.cantidad = item.cantidad - int(cant)
			item.save()

		print(id_item)
		print(cant)	
	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})