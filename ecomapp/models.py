from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class spcreatemodel(models.Model):
    shopname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    def __str__(self):
        return self.shopname
class spuploadmodel(models.Model):
    ptname=models.CharField(max_length=30)
    ptid=models.IntegerField()
    ptimage=models.FileField(upload_to='ecomapp/static')
    ptprice=models.IntegerField()
    desc=models.CharField(max_length=60)
    def __str__(self):
        return self.ptname
class usrcreatemodel(models.Model):
    username=models.CharField(max_length=30)
    email = models.EmailField()
    first_name=models.CharField(max_length=35)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=120)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
class cart(models.Model):
    ptname = models.CharField(max_length=30)
    ptid = models.IntegerField()
    ptimage = models.FileField(upload_to='ecomapp/static')
    ptprice = models.IntegerField()
    desc = models.CharField(max_length=60)
    def __str__(self):
        return self.ptname


