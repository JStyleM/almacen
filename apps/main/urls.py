from django.conf.urls import url
from .views import home, item_update, CreateItem

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^retirar$', item_update, name='retiro'),
    url(r'^create$', CreateItem.as_view(), name='crear'),
]