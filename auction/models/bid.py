from django.db import models
from users.models.auction_user import AuctionUser
from .auction import Auction

class Bid(models.Model):
    auctionuser = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
