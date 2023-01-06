from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('products', views.product_view.ProductListView.as_view(),
         name='products'),
    path('products/<int:pk>/detail',
         views.product_view.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.product_view.ProductCreateView.as_view(),
         name='product_create'),
    path('products/<int:pk>/update/',
         views.product_view.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/',
         views.product_view.ProductDeleteView.as_view(), name='product_delete'),
]
