from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleado(request):
    return render(request,"empleado.html")

def libros(request):
    return render(request,"libros.html")

def ventas(request):
    return render(request,"ventas.html")

def sucursal(request):
    return render(request,"sucursal.html")
