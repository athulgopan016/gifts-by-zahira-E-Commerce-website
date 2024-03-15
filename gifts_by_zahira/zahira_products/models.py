from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    
    def __int__(self):
        return self.id
    
    

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    
    @property
    def image_url(self):
        return self.product.image.url

    @property
    def product_name(self):
        return self.product.name

    @property
    def product_description(self):
        return self.product.description

