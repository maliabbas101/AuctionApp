from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from ..models.product import Product
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms

class ProductBaseView(View):
    model = Product
    fields = ['title','description','starting_price','category','photo', 'auctionuser']
    success_url = reverse_lazy('products')


class ProductListView(ProductBaseView, ListView):
    """
    """


class ProductDetailView(ProductBaseView, DetailView):
    """View to list the details from one product.
    Use the 'Product' variable in the template to access
    the specific Product here and in the Views below"""
    # model = Item
    # template_name = 'Items.html'


# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ProductCreateView(ProductBaseView, CreateView):
    """View to create a new product"""

    def get_form(self):
        form = super().get_form()
        form.fields['photo'].widget = forms.FileInput(attrs={'multiple': 'true', 'accept': 'image/*'})
        return form






# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ProductUpdateView(ProductBaseView, UpdateView):
    """View to update a product"""
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if request.user.email != obj.restaurant.owner.email:
    #         raise PermissionDenied
    #     return super(ItemUpdateView, self).dispatch(request, *args, **kwargs)


# @method_decorator(required_roles(allowed_roles=['admin']), name='dispatch')
class ProductDeleteView(ProductBaseView, DeleteView):
    """View to delete a Product"""
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if request.user.email != obj.restaurant.owner.email:
    #         raise PermissionDenied
    #     return super(ItemDeleteView, self).dispatch(request, *args, **kwargs)
