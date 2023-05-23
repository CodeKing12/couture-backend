from .models import Product, ProductGroup, Category, Cart
from store.api.serializers import ProductSerializer, GroupSerializer, CategorySerializer, CartSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializer

class GroupDetails(generics.RetrieveAPIView):
    lookup_field = "name"
    queryset = ProductGroup.objects.all()
    serializer_class = GroupSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetails(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SearchProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'created_at']
    # filterset_fields = ["name", "short_description", "category", "price", "composition"]

class RetrieveUpdateCart(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        return Cart.objects.get(user=self.request.user)