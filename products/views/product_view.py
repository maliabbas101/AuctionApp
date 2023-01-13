from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from ..models.product import Product
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib import messages
from AuctApp.decorators import required_roles
from django.shortcuts import render
from users.models.auction_user import AuctionUser
from users.models.review import Review
from django.shortcuts import redirect
class ProductBaseView(View):
    model = Product
    fields = ['title','description','starting_price','category','photo']
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

    def form_valid(self, form):
        form.instance.auctionuser = self.request.user
        return super(ProductCreateView, self).form_valid(form)





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



class PurchasedProductView(View):
    def get(self,request):
        products = Product.get_product_by_owner(request.user)
        context = {
            'product_list': products
        }
        return render(request, 'products/purchased_products.html', context)

    def post(self,request):
        auction_seller_id = request.POST.get('seller')
        auction_seller = AuctionUser.get_auction_user_by_id(auction_seller_id).first()
        owner_id = request.POST.get('buyer')
        auction_buyer = AuctionUser.get_auction_user_by_id(owner_id).first()
        review = request.POST.get('review')

        new_review = Review(auctionuser_buyer=auction_buyer, auctionuser_seller=auction_seller, review = review)
        new_review.save()
        messages.success(request, 'Review added.')
        return redirect('purchased_products')
