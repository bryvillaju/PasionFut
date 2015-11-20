from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.lista_partidos),
        url(r'^partido/(?P<pk>[0-9]+)/$', views.detalle_partido),
	url(r'^partido/nuevo/$', views.nuevo_partido, name='nuevo_partido'),
	url(r'^partido/(?P<pk>[0-9]+)/editar/$', views.editar_partido, name='editar_partido'),
	url(r'^partido/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_partido, name='eliminar_partido'),
    ]
