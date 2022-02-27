from collections import UserDict
from pyexpat import model
from statistics import mode
from unicodedata import category
from urllib.request import Request
from django.db import models
from accounts.models import User

# Create your models here.

class VehicalType(models.Model):
    Type_Name = models.CharField(max_length=50)
    Type_Image = models.ImageField(upload_to='type_img')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Type_Name

    class Meta:
        db_table = 'VehicalType'

class brand(models.Model):
    BrandName = models.CharField(max_length=50)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    AddDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BrandName

    class Meta:
        db_table = 'brand'

class category_list(models.Model):
    Category_Name = models.CharField(max_length=50)
    AddDate = models.DateTimeField(auto_now_add=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehical_TypeID = models.ForeignKey(VehicalType, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.Category_Name

    class Meta:
        db_table = 'category_list'