from django.db import models

#Keperluan Tugas 4
# Menghubungkan Product dengan User
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #menghubungkan satu produk dengan satu user melalui sebuah relationship
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    local_image = models.ImageField(upload_to='products/', blank=True, null=True)
    url_image = models.URLField(blank=True, null=True)
# Create your models here.

# (Models Challenge) Misalkan, aplikasi kamu ingin merepresentasikan data-data Employee dengan atribut:
# name : CharField
# age : IntegerField
# hobby : TextField

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     hobby = models.TextField()