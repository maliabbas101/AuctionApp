from django.db import models
from users.models.auction_user import AuctionUser
from django.urls import reverse


class Bid(models.Model):
    auctionuser = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    auction = models.ForeignKey("auction.Auction", on_delete=models.CASCADE)
    bid_amount = models.FloatField()

    def get_absolute_url(self):
        return reverse("auction_detail", kwargs={"pk": self.auction.pk})

    @staticmethod
    def get_auction_winner(id):
        bids = Bid.objects.filter(auction__id=id)
        max_bid = 0
        for bid in bids:
            if bid.bid_amount > max_bid:
                max_bid = bid.bid_amount
                winner = bid.auctionuser
        return max_bid, winner

    @staticmethod
    def get_bids_by_auction_user(auctionuser, auction):
        bids = Bid.objects.filter(auctionuser=auctionuser).filter(auction=auction)
        return bids
