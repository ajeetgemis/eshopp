from django.db import models

class categories(models.Model):
    p_categ=models.CharField(max_length=20)

    def __str__(self):
        return self.p_categ