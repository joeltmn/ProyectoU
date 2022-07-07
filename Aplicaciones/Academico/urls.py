# Este archivo nos va a servir para gestionar las rutas
# Solamente de esta aplicacion llamada "ACADEMICO"

# Vamos a importar el metodo "path" que nos permite
# definir una ruta

from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminacionCurso/<codigo>', views.eliminacionCurso)
]