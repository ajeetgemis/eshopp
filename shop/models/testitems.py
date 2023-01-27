from django.db import models
from .testorder import testorders

class orderitems(models.Model):
    order=models.ForeignKey(testorders,max_length=200,on_delete=models.CASCADE)
    qty=models.CharField(max_length=10)
    prod_image=models.ImageField(upload_to='uploads\products')
    price=models.CharField(max_length=20,default='0')
    total_price=models.CharField(max_length=20,default='0')

