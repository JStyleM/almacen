from django.conf.urls import url
from .views import home, item_retiro, crear_item, movimientos, crear_movimiento, item_add, LoginView, LogoutView

urlpatterns = [
	url(r'^almacen$', home, name='home'),
	url(r'^movimientos$', movimientos, name='movimientos'),
    url(r'^retirar$', item_retiro, name='retiro'),
    url(r'^add$', item_add, name='add'),
    url(r'^create_item$', crear_item, name='crear_item'),
    url(r'^create_mov$', crear_movimiento, name='crear_mov'),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
]