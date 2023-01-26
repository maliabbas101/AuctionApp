from django.db import models
from .auction_user import AuctionUser


class Review(models.Model):
    auctionuser_buyer = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    auctionuser_seller = models.ForeignKey(
        AuctionUser, on_delete=models.CASCADE, related_name="seller_review_set"
    )
    review = models.CharField(max_length=255)
