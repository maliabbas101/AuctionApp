from django.db import models
from products.models.product import Product


class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
      return self.product.title

