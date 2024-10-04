from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name='index'),
    path("contactos/",views.contactos, name='contactos'),
    path("empleado/",views.empleado, name='empleado'),
    path("libros/",views.libros, name='libros'),
    path("ventas/",views.ventas, name='ventas'),
    path("sucursal/",views.sucursal, name='sucursal'),
]

