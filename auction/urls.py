from django.urls import path
from . import views

urlpatterns = [
    path("", views.auction_view.AuctionListView.as_view(), name="auctions"),
    path(
        "seller-auctions",
        views.auction_view.SellerAuctionListView.as_view(),
        name="seller-auctions",
    ),
    path(
        "<int:pk>/detail",
        views.auction_view.AuctionDetailView.as_view(),
        name="auction_detail",
    ),
    path(
        "create/", views.auction_view.AuctionCreateView.as_view(), name="auction_create"
    ),
    path(
        "<int:pk>/delete/",
        views.auction_view.AuctionDeleteView.as_view(),
        name="auction_delete",
    ),
    path(
        "<int:pk>/approve/", views.auction_view.approval_auction, name="auction_approve"
    ),
    path(
        "<int:pk>/decline/", views.auction_view.decline_auction, name="auction_decline"
    ),
    path("<int:pk>/bids/", views.bid_view.BidListView.as_view(), name="bids"),
]
