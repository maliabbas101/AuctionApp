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

    @staticmethod
    def get_auction_winner(id):
        bids = Bid.objects.filter(auction__id=id)
        max_bid = 0
        for bid in bids:
            if bid.bid_amount > max_bid:
                max_bid=bid.bid_amount
                winner = bid.auctionuser
        return max_bid, winner


