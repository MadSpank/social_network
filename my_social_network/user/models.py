from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.EmailField()
  bio = models.TextField(max_length=300)
  country = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  status = models.CharField(max_length=100)
