from django.views.generic import CreateView, ListView, DetailView,DeleteView
from ..models.bid import Bid
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib import messages

class BidBaseView(View):
    model = Bid
    fields = ['auctionuser', 'auction', 'bid_amount']

class BidListView(BidBaseView, ListView):
    """
    """



# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
# class BidCreateView(BidBaseView, CreateView):
#     """"""
#     def get_form(self):
#         form = super().get_form()
#         form.fields['auction'].widget = forms.TextInput(attrs={'hiddden': 'true'})
#         # form.fields['end_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
#         return form

#     def post(self, request, *args, **kwargs):
#         messages.success(request, "Bid placed successfully.")
#         return super().post(request, *args, **kwargs)
