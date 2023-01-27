from django.db import models
from .register import registermodel
import datetime

class testorders(models.Model):
    customer=models.ForeignKey(registermodel,max_length=200,on_delete=models.CASCADE)
    total_price=models.CharField(max_length=20,default=0,blank=True)
    order_id=models.CharField(primary_key=True,max_length=200)
    razorpay_payment_id=models.CharField(max_length=200,default=True,null=True)
    razorpay_signature=models.CharField(max_length=200,default=True,null=True)
    payment_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.datetime.today)
    choices=(('pending','pending'),('authorised','Authorised'),('Captured','Capured'))
    order_status=models.CharField(choices=choices,max_length=100)         