from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.ProductList.as_view(), name="all-products"),
    path('products/<slug:slug>/', views.ProductDetails.as_view(), name="product-info"),
    path('groups/<str:name>/', views.GroupDetails.as_view(), name="group-products"),
    path('categories/', views.CategoryList.as_view(), name="all_categories"),
    path('categories/<slug:slug>/', views.CategoryDetails.as_view(), name="category_products"),
    path('search/', views.SearchProducts.as_view(), name="search_products"),
    path('cart/', views.RetrieveUpdateCart.as_view(), name="add_to_cart")
]