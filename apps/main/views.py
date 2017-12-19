from django.shortcuts import render
from .models import Item


# Create your views here.

def home(request):
	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})

def item_update(request, item_id, monto):
	print(item_id)
	print(monto)
	item = Item.objects.get(id=item_id)
	item.cantidad = item.cantidad - int(monto)
	item.save()
	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})	