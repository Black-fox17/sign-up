from django.db import models

# Desktop/Django/sign_up
# Create your models here.
class new_page(models.Model):
    Username = models.CharField(max_length = 30,unique = True)
    Password = models.CharField(max_length = 148)
    Email = models.CharField(max_length = 128,unique = True)