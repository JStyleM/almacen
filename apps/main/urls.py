from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^(?P<item_id>\d+)/(?P<monto>\d+)$', views.item_update, name='retiro'),
]