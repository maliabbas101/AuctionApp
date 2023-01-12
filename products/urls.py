from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from products.views.index_view import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('products', views.product_view.ProductListView.as_view(),
         name='products'),
    path('purchased-products', views.product_view.PurchasedProductView.as_view(),
         name='purchased_products'),
    path('products/create/', views.product_view.ProductCreateView.as_view(),
         name='product_create'),
    path('products/<int:pk>/update/',
         views.product_view.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/',
         views.product_view.ProductDeleteView.as_view(), name='product_delete'),
]
