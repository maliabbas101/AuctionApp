from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


class AuctionUser(AbstractUser):
    username = models.CharField(_('Username'), max_length=255, unique=True)
    email = models.EmailField(_('Email'), max_length=255, unique=True)

    def __str__(self):
        return self.username

    def register(self):
        self.save()

    @staticmethod
    def get_auction_user_by_id(id):
        return AuctionUser.objects.filter(id=id)
