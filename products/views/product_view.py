from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from ..models.product import Product
from django.urls import reverse_lazy
from django.views import View
# from customers.decorators import required_roles
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib import messages
from AuctApp.decorators import required_roles

class ProductBaseView(View):
    model = Product
    fields = ['title','description','starting_price','category','photo', 'auctionuser']
    success_url = reverse_lazy('products')

@method_decorator(required_roles(allowed_roles=['admin', 'seller']), name='dispatch')
class ProductListView(ProductBaseView, ListView):
    """
    """

@method_decorator(required_roles(allowed_roles=['seller']), name='dispatch')
class ProductCreateView(ProductBaseView, CreateView):
    """View to create a new product"""

    def get_form(self):
        form = super().get_form()
        form.fields['photo'].widget = forms.FileInput(attrs={'multiple': 'true', 'accept': 'image/*'})
        return form

    def post(self, request, *args, **kwargs):
        messages.success(request, "Product created successfully.")
        return super().post(request, *args, **kwargs)






@method_decorator(required_roles(allowed_roles=['seller']), name='dispatch')
class ProductUpdateView(ProductBaseView, UpdateView):
    """View to update a product"""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.email != obj.auctionuser.email:
            raise PermissionDenied
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


@method_decorator(required_roles(allowed_roles=['admin','seller']), name='dispatch')
class ProductDeleteView(ProductBaseView, DeleteView):
    """View to delete a Product"""

    def post(self, request, *args, **kwargs):
        messages.error(request, "Product deleted successfully.")
        return super().post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        group = request.user.groups.first()
        if request.user.email != obj.auctionuser.email and str(group) !='admin':
            raise PermissionDenied
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
