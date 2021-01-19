from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):#heredea de models.Models
    #para el modelo proxy onetoone solo me permite crear un perfil por cada usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200 , blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(blank=True, max_length=50)

    picture=models.ImageField(
         upload_to='users/pictures' ,#las guarda en estas carpetas de users/picture que esta dentro de media
         blank=True,
         null=True
    )

    created = models.DateTimeField(auto_now=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


#from django.contrib.auth.models import User

#class Employee(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    department = models.CharField(max_length=100)

