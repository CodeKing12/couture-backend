from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.ProductList.as_view(), name="all-products"),
    path('<slug:slug>', views.ProductDetails.as_view(), name="product-info"),
    path('groups/<str:name>/', views.GroupDetails.as_view(), name="group-products"),
]