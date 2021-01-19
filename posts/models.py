from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
                                    #Elimina el objeto que contenga la foreignKey
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    #Para asegurarse que no se esta creando relaciones circulares 
    profile=models.ForeignKey('users.Profile',on_delete=models.CASCADE)


    title=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='posts/photos')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.title,self.user.username)