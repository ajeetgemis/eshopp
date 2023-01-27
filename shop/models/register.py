from django.db import models

class registermodel(models.Model):
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    address1=models.TextField(max_length=100)
    address2=models.TextField(max_length=100)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.email