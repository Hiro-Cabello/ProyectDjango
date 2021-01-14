# Create your models here.
#https://docs.djangoproject.com/en/2.0/ref/models/fields/
#https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#
#Django


from django.db import models
class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    is_admin=models.BooleanField(default=False)

    bio=models.TextField(blank=True)
    birthdate=models.DateField(blank=True,null=True)
    created=models.DateTimeField(auto_now=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


#Para la creacion de objetos 
#https://docs.djangoproject.com/en/2.0/topics/db/queries/

#La consola interaccitiva cargada con django se usa asi 
#python manage.py shell




#Nota
#Luego de creado los modelos se tiene que usar las migraciones para que los cambios 
#se vean reflejados en la base de datos
#Aplica los cambios en mi modelo
#PS E:\JAIRO\Cursos de la Universidad\CICLO 8\Django\Platzigram> python .\manage.py makemigrations
#Migrations for 'posts':
#  posts\migrations\0001_initial.py
#    - Create model User
#dentro de la carpeta migrations se ve reflejado los cambios 

#Aplica los cambios en mi base de datos
#PS E:\JAIRO\Cursos de la Universidad\CICLO 8\Django\Platzigram> python .\manage.py migrate




