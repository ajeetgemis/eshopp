# Generated by Django 3.2.16 on 2023-01-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_registermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_price',
            field=models.BigIntegerField(default=0),
        ),
    ]
