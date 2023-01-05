# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models.auction_user import AuctionUser

class AuctionUserCreationForm(UserCreationForm):

    class Meta:
        model = AuctionUser
        fields = ("username", "email")

class AuctionUserChangeForm(UserChangeForm):

    class Meta:
        model = AuctionUser
        fields = ("username", "email")
