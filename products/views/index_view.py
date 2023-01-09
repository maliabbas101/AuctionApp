from django.shortcuts import render, redirect
from products.models.product import Product
from products.models.category import Category
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_products_by_category(category_id)
        else:
            products = Product.get_all_products()

        categories = Category.get_all_categories()
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'home.html', context)


