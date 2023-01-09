from django.views.generic import CreateView, ListView, DetailView,DeleteView
from ..models.auction import Auction
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms

class AuctionBaseView(View):
    model = Auction
    fields = ['product', 'start_time', 'end_time']
    success_url = reverse_lazy('auctions')


class AuctionListView(AuctionBaseView, ListView):
    """
    """


class AuctionDetailView(AuctionBaseView, DetailView):
    """"""


# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionCreateView(AuctionBaseView, CreateView):
    """"""

    def get_form(self):
        form = super().get_form()
        form.fields['start_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        form.fields['end_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        return form



# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionDeleteView(AuctionBaseView, DeleteView):
    """"""
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if request.user.email != obj.restaurant.owner.email:
    #         raise PermissionDenied
    #     return super(ItemDeleteView, self).dispatch(request, *args, **kwargs)
