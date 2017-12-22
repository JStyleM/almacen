from django.conf.urls import url
from .views import home, item_update, CreateItem, movimientos, crear_movimiento

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^movimientos$', movimientos, name='movimientos'),
    url(r'^retirar$', item_update, name='retiro'),
    url(r'^create_item$', CreateItem.as_view(), name='crear_item'),
    url(r'^create_mov$', crear_movimiento, name='crear_mov'),
]