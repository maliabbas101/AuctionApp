from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_category_by_id(id):
        return Category.objects.filter(id=id)
