from django.db import models

# Create your models here.

# class Courseregister(models.Model):
#     id=models.AutoField(primary_key=True)
#     email=models.EmailField(default=None)
#     phone=models.IntegerField(default=None)
#     course=models.CharField(max_length=30)
    
    
# models.py
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username



class Data(models.Model):
    username=models.CharField(max_length=500)
    fullname=models.CharField( max_length=50)
    mobile=models.IntegerField(default=None)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    