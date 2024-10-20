from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('add/', views.add_vehiculo, name='add_vehiculo'),  # Ruta para agregar un vehículo
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),  # Ruta para listar vehículos
]