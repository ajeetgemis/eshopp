from django.db import models
from .product import products
from .register import registermodel
import datetime

class cartmodel(models.Model):
    customer=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField()
    address1=models.TextField(default='',blank=True)
    address2=models.TextField(default='',blank=True)
    phonenumber=models.CharField(max_length=10,default=True)
    date=models.DateTimeField(default=datetime.datetime.today)
