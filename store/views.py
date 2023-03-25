from .models import Product, ProductGroup, Category
from store.api.serializers import ProductSerializer, GroupSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import filters

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

class CategoryDetails(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SearchProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "short_description"]
