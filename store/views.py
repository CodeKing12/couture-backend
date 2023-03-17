from .models import Product
from store.api.serializers import ProductSerializer
from rest_framework import generics

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializer