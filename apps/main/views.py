from django.shortcuts import render
from .models import Item


# Create your views here.

def home(request):

	query = Item.objects.all()
	return render(request, 'index.html', {'query':query})

