from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuctionUserCreationForm, AuctionUserChangeForm
from .models.auction_user import AuctionUser

class AuctionUserAdmin(UserAdmin):
    add_form = AuctionUserCreationForm
    form = AuctionUserChangeForm
    model = AuctionUser
    list_display = ["email", "username",]

admin.site.register(AuctionUser, AuctionUserAdmin)
