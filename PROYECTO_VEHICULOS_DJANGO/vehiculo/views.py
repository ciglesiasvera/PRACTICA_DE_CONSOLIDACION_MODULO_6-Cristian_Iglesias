from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo
from .forms import VehiculoForm

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    context = {
        'vehiculos': vehiculos,
    }
    return render(request, 'vehiculo/listar.html', context)

@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de guardar
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'form': form})
