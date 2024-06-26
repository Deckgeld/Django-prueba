"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from inicio import views
from registros import views as registros_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',registros_views.registros, name="Principal"),
    path('registrar/',registros_views.registrar,name="Registrar"),
    path('contacto/',registros_views.contacto,name="Contacto"),
    path('formulario/',views.formulario,name="Formulario"),

    path('comentarios/',registros_views.comentarios,name="Comentarios"),
    #path('ejemplo/',views.ejemplo,name="ejemplo"),
]

#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que
#almacenan la ubicación de nuestras imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)