"""Platzigram URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#Esto es el modulo de urls



#Para el admin 
from django.contrib import admin


#para solucionar el problema de no podervisualizar las imagenes de los usuarios
from django.conf.urls.static import static
from django.conf import settings

#from django.contrib import admin
from django.urls import path
#vamos a importar las vistas
from Platzigram import views as local_views
#Voy a importar las vistas de mi aplicacion post y las renombrare como posts_views
#previo a la importacion tengo que establecerla en el archivo settings.py
from users import views as users_views

from posts import views  as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Una vista en django es una función 
    #Primer parametro es la direccion y segundo es la funcion 
    path('hello-world/', local_views.hello_world),
    #http://127.0.0.1:8000/sorted/?numbers=10,5,6,4,7,8,1
    path('sorted/', local_views.sorted_integers),
    path('hi/<str:name>/<int:age>/',local_views.say_hi),
    #path('lista/', local_views.lista_posts),

    
    path('posts/', posts_views.list_posts)
] +  static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)