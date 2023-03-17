from rest_framework.serializers import ModelSerializer
from store.models import Product, Category, Composition

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    composition = CompositionSerializer(many=True)

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
                'category': {
                    "name": instance.category.title,
                    "slug": instance.category.slug
                },
                'price': instance.price,
                'previous_price': instance.previous_price,
                'composition': [
                    {
                        "name": c.name,
                        "percent": c.percentage
                    } for c in instance.composition.all()
                ]
            }
        
        return super().to_representation(instance)