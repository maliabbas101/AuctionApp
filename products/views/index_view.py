from django.shortcuts import render, redirect
from auction.models.auction import Auction
from products.models.category import Category
from products.models.product import Product
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        if str(request.user.groups.first()) == 'buyer':
            category_id = request.GET.get('category')
            if category_id:
                auctions = Auction.get_auctions_by_category(category_id)
            else:
                auctions = Auction.get_all_auctions()

            categories = Category.get_all_categories()
            context = {
                'auctions': auctions,
                'categories': categories,
            }
        elif str(request.user.groups.first()) == 'seller':
            product_list = Product.get_products_of_auctionuser(request.user)
            context= {
              'product_list': product_list
            }
            return render(request,'products/product_list.html',context)

        else:
            context = {
                'page': 'Admin'
            }

        return render(request, 'home.html', context)



