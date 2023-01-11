from django.db import models
from products.models.product import Product


class Auction(models.Model):
    STATUS_EXPIRED = "SE"
    STATUS_APPROVED = "SA"
    STATUS_PENDING = "SP"

    STATUS_CHOICES = [

        (STATUS_EXPIRED, "Expired"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_PENDING, "Pending"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
    max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
      return self.product.title

    @staticmethod
    def number_of_auctions():
      return Auction.objects.all().count()


    @staticmethod
    def get_all_auctions():
        return Auction.objects.all()

    @staticmethod
    def get_auction_by_id(id):
        return Auction.objects.filter(id=id)

    @staticmethod
    def get_auctions_by_category(category_id):
      if (category_id):
        return Auction.objects.filter(product__category__id=category_id)
      else:
          return Auction.get_all_auctions()


