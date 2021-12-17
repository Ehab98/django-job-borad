from django.db import models
from django.db.models.fields import EmailField


class Info(models.Model):
    
    place = models.CharField(max_length=50)
    phone_number =models.CharField( max_length=20)
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.email
    