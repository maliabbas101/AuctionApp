from django.db import models
from users.models.auction_user import AuctionUser
from .auction import Auction
from django.urls import reverse

class Bid(models.Model):
    auctionuser = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_amount = models.FloatField()


    def get_absolute_url(self):
        return reverse('auction_detail', kwargs={'pk': self.auction.pk})
