from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.image import Image

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
