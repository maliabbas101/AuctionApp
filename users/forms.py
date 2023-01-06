# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models.auction_user import AuctionUser

class AuctionUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all().exclude(name='admin'),
                                    required=True)

    class Meta:
        model = AuctionUser
        fields = ("username", "email","groups")

class AuctionUserChangeForm(UserChangeForm):

    class Meta:
        model = AuctionUser
        fields = ("username", "email")
