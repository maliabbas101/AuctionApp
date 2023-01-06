from django.db import models
from .product import Product

class Image(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='media/products/',
                              default='media/prod_c8m26c.png')
