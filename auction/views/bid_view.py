from django.views.generic import ListView
from ..models.bid import Bid
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from AuctApp.decorators import required_roles
from django.shortcuts import render


class BidBaseView(View):
    model = Bid
    fields = ["auctionuser", "auction", "bid_amount"]


@method_decorator(required_roles(allowed_roles=["seller"]), name="dispatch")
class BidListView(BidBaseView, ListView):
    """ """

    def get(self, request, *args, **kwargs):
        auction_id = kwargs.get("pk")
        bids = Bid.objects.filter(auction=auction_id)
        context = {"bid_list": bids}
        return render(request, "auction/bid_list.html", context)
