from django.views.generic import ListView
from ..models.bid import Bid
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from AuctApp.decorators import required_roles


class BidBaseView(View):
    model = Bid
    fields = ['auctionuser', 'auction', 'bid_amount']

@method_decorator(required_roles(allowed_roles=['seller']), name='dispatch')
class BidListView(BidBaseView, ListView):
    """
    """
