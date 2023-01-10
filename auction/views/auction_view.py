from django.views.generic import CreateView, ListView, DetailView,DeleteView
from django.shortcuts import render, redirect
from ..models.auction import Auction
from ..models.bid import Bid
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.models.auction_user import AuctionUser
from products.models.product import Product
class AuctionBaseView(View):
    model = Auction
    fields = ['product', 'start_time', 'end_time']
    success_url = reverse_lazy('auctions')


class AuctionListView(AuctionBaseView, ListView):
    """
    """


class AuctionDetailView(AuctionBaseView, DetailView):
    """"""

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user_id = request.POST.get('user')
        auction_user = AuctionUser.get_auction_user_by_id(user_id).first()
        auction_id = request.POST.get('auction')
        auction = Auction.get_auction_by_id(auction_id).first()
        bid_amount = request.POST.get('bid_amount')

        new_bid = Bid(auctionuser=auction_user,auction=auction, bid_amount=float(bid_amount))
        new_bid.save()

        auction_product = Product.get_product_by_id(auction.product.id).first()
        auction_product.increase_starting_price(bid_amount)

        messages.success(request, "Bid placed successfully.")
        return HttpResponseRedirect(self.request.path_info)

# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionCreateView(AuctionBaseView, CreateView):
    """"""
    def get_form(self):
        form = super().get_form()
        form.fields['start_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['end_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        return form

    def post(self, request, *args, **kwargs):
        messages.success(request, "Auction created successfully.")
        return super().post(request, *args, **kwargs)



# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionDeleteView(AuctionBaseView, DeleteView):
    """"""
    def post(self, request, *args, **kwargs):
        messages.error(request, "Auction deleted successfully.")
        return super().post(request, *args, **kwargs)

    #     obj = self.get_object()
    #     if request.user.email != obj.restaurant.owner.email:
    #         raise PermissionDenied
    #     return super(ItemDeleteView, self).dispatch(request, *args, **kwargs)
