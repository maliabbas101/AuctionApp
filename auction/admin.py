from django.contrib import admin

# Register your models here.
from .models.auction import Auction
from .models.bid import Bid
from .models.watchlist import WatchList

admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(WatchList)
