from django.views.generic import ListView, UpdateView, DeleteView
from users.models.auction_user import AuctionUser
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied


class AuctionUserBaseView(View):
    model = AuctionUser
    fields = ["username", "email", "first_name", "last_name"]
    success_url = reverse_lazy('auction_users')


class AuctionUserListView(AuctionUserBaseView, ListView):
    """
    """


# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionUserDeleteView(AuctionUserBaseView, DeleteView):
    """"""
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if request.user.email != obj.restaurant.owner.email:
    #         raise PermissionDenied
    #     return super(ItemDeleteView, self).dispatch(request, *args, **kwargs)
