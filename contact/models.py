from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=25)
    
    def __str__(self):
        return self.first_name