from django.db import models
from django.core.validators import MinValueValidator
from .category import Category
from users.models.auction_user import AuctionUser


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    starting_price = models.IntegerField(default=0, validators=[
        MinValueValidator(1)
    ])
    photo = models.ImageField(upload_to='media/products/',
                              default='media/prod_c8m26c.png')
    auctionuser = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def increase_starting_price(self, number):
        self.starting_price += number
        return self

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_product_by_id(id):
        return Product.objects.filter(id=id)

    @staticmethod
    def get_products_by_category(category_id):
        if (category_id):
            return Product.objects.filter(categories=category_id)
        else:
            return Product.get_all_items()
