from rest_framework.serializers import ModelSerializer
from store.models import Product, Category, Composition

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '_all__'


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and 'display' in request.path:
            return {
                'id': instance.id,
                'name': instance.name,
                'slug': instance.slug,
                'category': instance.category,
                'price': instance.price,
                'previous_price': instance.previous_price,
                'composition': instance.composition
            }
        
        return super().to_representation(instance)