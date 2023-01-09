from django.db import models
from users.models.auction_user import AuctionUser
from products.models.product import Product

class WatchList(models.Model):
  auctionuser = models.ForeignKey(AuctionUser,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)

