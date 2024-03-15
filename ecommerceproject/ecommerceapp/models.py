from django.db import models 

class product(models.Model):
    name=models.CharField(max_length=15)
    price=models.DecimalField(max_digits=5,decimal_field=2)
    description=models.TextField()
    brand=models.CharField(max_length=25)

