from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class Products(models.Model):
    p_name = models.CharField(max_length=100)
    p_rating = models.DecimalField(max_digits=5, decimal_places=1)
    p_description = models.CharField(max_length=200)
    p_buycount = models.IntegerField()
    p_brand = models.CharField(max_length=100)
    p_category = models.CharField(max_length=100)
    p_image = models.ImageField(upload_to="cosx_home/images/")


