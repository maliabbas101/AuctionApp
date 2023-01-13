from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuctionUserCreationForm, AuctionUserChangeForm
from .models.auction_user import AuctionUser
from .models.review import Review

class AuctionUserAdmin(UserAdmin):
    add_form = AuctionUserCreationForm
    form = AuctionUserChangeForm
    model = AuctionUser
    list_display = ["email", "username",]

admin.site.register(AuctionUser, AuctionUserAdmin)
admin.site.register(Review)
