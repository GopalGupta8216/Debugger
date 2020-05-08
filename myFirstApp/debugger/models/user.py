from django.db import models

class User(models.Model):
    name = models.CharField(
    max_length = 40,
    unique = True
    )
    image = models.ImageField(
    upload_to = 'image'
    )
    contact = models.CharField(
    max_length = 15
    )
    email = models.EmailField( 
    max_length = 254,
    unique=True
    )

    def __str__(self):
        return self.name
