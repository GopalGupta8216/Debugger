from django.db import models

class User(models.Model):
    enrollment = models.CharField(
    max_length = 8,
    unique = True,
    default = 12345678
    )
    name = models.CharField(
    max_length = 40,
    unique = False
    )
    image = models.ImageField(
    upload_to = 'image'
    )
   
    email = models.EmailField( 
    max_length = 254,
    unique=True
    )
    is_admin =  models.BooleanField(default = False)
    

    def __str__(self):
        return self.name
