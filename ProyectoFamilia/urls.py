from django.contrib import admin
from django.urls import path, include

from ProyectoFamilia.views import hola_mundo, hola_desde_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo, name='hola_mundo'),
    path('hola-desde-template/', hola_desde_template),

    path('family/', include('family.urls')),
]
