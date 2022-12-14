"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import index as index_blog
from prueba.views import (inicio, listar_familia, BuscarFamiliar, AltaFamiliar,
                         ActualizarFamiliar, Borrar, FamiliarList, 
                         FamiliarCrear, FamiliarBorrar, FamiliarActualizar )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', index_blog),
    path('test/<nombre>', inicio),
    path('prueba/listar/', listar_familia), 
    path('prueba/buscar', BuscarFamiliar.as_view()),
    path('prueba/alta', AltaFamiliar.as_view()),
    path('prueba/actualizar/<int:pk>',ActualizarFamiliar.as_view()),
    path('prueba/borrar/<int:pk>', Borrar.as_view()),
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/crear', FamiliarCrear.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view(), name='familiar-actualizar'), # NUEVA RUTA PARA LISTAR FAMILIAR
    
]
