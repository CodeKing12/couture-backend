from .models import Product, ProductGroup
from store.api.serializers import ProductSerializer, GroupSerializer
from rest_framework import generics

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