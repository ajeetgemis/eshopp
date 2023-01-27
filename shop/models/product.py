from django.db import models
from .category import categories

class products(models.Model):
    p_name=models.CharField(max_length=20)
    p_description=models.CharField(max_length=30)
    p_category=models.ForeignKey(categories,on_delete=models.CASCADE,default=1)
    p_price=models.BigIntegerField(default=0)    
    p_image=models.ImageField(upload_to='uploads\products')

    def __str__(self):
        return self.p_name