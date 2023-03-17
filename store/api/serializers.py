from rest_framework.serializers import ModelSerializer
from store.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "image", "short_description", "category", "price", "previous_price"]