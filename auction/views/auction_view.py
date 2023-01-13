from django.views.generic import CreateView, ListView, DetailView,DeleteView
from django.shortcuts import render, redirect
from ..models.auction import Auction
from ..models.bid import Bid
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.models.auction_user import AuctionUser
from products.models.product import Product
from AuctApp.decorators import required_roles
from django.core.exceptions import PermissionDenied
from django.db.models import Q
class AuctionBaseView(View):
    model = Auction
    fields = ['product', 'start_time', 'end_time']
    success_url = reverse_lazy('auctions')

@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionListView(AuctionBaseView, ListView):
    """
    """

@method_decorator(required_roles(allowed_roles=['buyer','seller']), name='dispatch')
class AuctionDetailView(AuctionBaseView, DetailView):
    """"""
    def get_context_data(self, *args, **kwargs):
        context = super(AuctionDetailView,
                self).get_context_data(*args, **kwargs)
        auction = context.get('auction')
        if auction.status == "SE":
            highest_bid, winner = Bid.get_auction_winner(auction.id)
            context["winner"] = winner
            context["highest_bid"]= highest_bid
        return context

    def post(self, request, *args, **kwargs):
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

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        group=request.user.groups.first()
        if request.user.email != obj.product.auctionuser.email and str(group) !='buyer':
            raise PermissionDenied
        return super(AuctionDetailView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['seller']), name='dispatch')
class AuctionCreateView(AuctionBaseView, CreateView):
    """"""

    success_url = reverse_lazy("home")

    def get_form(self):
        form = super().get_form()
        form.fields['start_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['end_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['product'].queryset= Product.objects.all().exclude(status='SS').exclude(~Q(auctionuser = self.request.user))
        return form

    def post(self, request, *args, **kwargs):
        messages.success(request, "Auction created successfully.")
        return super().post(request, *args, **kwargs)



@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionDeleteView(AuctionBaseView, DeleteView):
    """"""
    def post(self, request, *args, **kwargs):
        messages.error(request, "Auction deleted successfully.")
        return super().post(request, *args, **kwargs)

@method_decorator(required_roles(allowed_roles=['seller']), name='dispatch')
class SellerAuctionListView(View):
    """"""

    def get(self, request):
        auction_list = Auction.get_auction_by_product_user(request.user.id)
        context = {
            'auction_list' : auction_list
        }
        return render(request,'auction/sellerauction_list.html', context)






required_roles(allowed_roles=['admin'])
def approval_auction(request, pk):
    auction = Auction.objects.get(pk=pk)
    auction.status = 'SA'
    auction.save()
    messages.success(request, "Auction has been approved and listed to buyers.")
    return redirect('auctions')

required_roles(allowed_roles=['admin'])
def decline_auction(request, pk):
    auction = Auction.objects.get(pk=pk)
    auction_product = Product.get_product_by_id(auction.product.id).first()
    auction_product.starting_price = 1.0
    auction_product.save()
    auction.delete()
    messages.error(request, "Auction has been declined and deleted.")
    return redirect('auctions')
