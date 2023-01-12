from django.views.generic import ListView, UpdateView, DeleteView
from users.models.auction_user import AuctionUser
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect
from AuctApp.decorators import required_roles

class AuctionUserBaseView(View):
    model = AuctionUser
    fields = ["username", "email", "first_name", "last_name"]
    success_url = reverse_lazy('auction_users')

@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionUserListView(AuctionUserBaseView, ListView):
    """
    """


@method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class AuctionUserDeleteView(AuctionUserBaseView, DeleteView):
    """"""

    def post(self, request, *args, **kwargs):
        messages.error(request, "User deleted successfully.")
        return super().post(request, *args, **kwargs)

required_roles(allowed_roles=['admin'])
def make_admin(request, pk):
    auction_user = AuctionUser.objects.get(pk=pk)
    auction_user.groups.clear()
    auction_user.groups.set('1')
    auction_user.save()
    messages.error(request, "Admin added successfully")
    return redirect('auction_users')
