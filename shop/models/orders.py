from django.db import models
from .register import registermodel
from .cartmodel import cartmodel


class orders(models.Model):
    customer=models.ForeignKey(registermodel,max_length=200,on_delete=models.CASCADE)
    order_items=models.ForeignKey(cartmodel,max_length=200,on_delete=models.CASCADE)
    total_price=models.CharField(max_length=20,default=0,blank=True)
    order_id=models.CharField(primary_key=True,max_length=200)
    razorpay_payment_id=models.CharField(max_length=200,default=True,null=True)
    razorpay_signature=models.CharField(max_length=200,default=True,null=True)
    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.order_id