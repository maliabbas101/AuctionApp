from django.urls import path
from .import views
from .views.signup_view import SignUpView
urlpatterns = [
    path( '', views.auction_user_view.AuctionUserListView.as_view(),
         name='auction_users'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('<int:pk>/update/',
         views.auction_user_view.AuctionUserUpdateView.as_view(), name='auction_user_update'),
    path('<int:pk>/delete/',
         views.auction_user_view.AuctionUserDeleteView.as_view(), name='auction_user_delete'),
]

