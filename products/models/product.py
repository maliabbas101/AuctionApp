from django.db import models
from django.core.validators import MinValueValidator
from .category import Category
from users.models.auction_user import AuctionUser


class Product(models.Model):
    STATUS_DELIVERED = "SD"
    STATUS_SOLD = "SS"
    STATUS_PENDING = "PN"

    STATUS_CHOICES = [
        (STATUS_DELIVERED, "Delivered"),
        (STATUS_SOLD, "Sold"),
        (STATUS_PENDING, "Pending"),
    ]
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    starting_price = models.FloatField(default=0.0, validators=[MinValueValidator(1.0)])
    auctionuser = models.ForeignKey(AuctionUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        AuctionUser,
        on_delete=models.CASCADE,
        related_name="owner_product_set",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.starting_price = round(self.starting_price, 2)
        super(Product, self).save(*args, **kwargs)

    def increase_starting_price(self, number):
        self.starting_price = float(number)
        self.save()

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
    def get_product_by_owner(owner):
        return Product.objects.filter(owner=owner)

    @staticmethod
    def get_products_of_auctionuser(user):
        return Product.objects.filter(auctionuser=user)

    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.get_all_items()
