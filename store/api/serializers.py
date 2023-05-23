from rest_framework.serializers import HyperlinkedRelatedField, ModelSerializer
from store.models import Product, Category, Composition, ProductGroup, Cart, CartItem

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and 'categor' not in request.path:
            return {
                "name": instance.name,
                "slug": instance.slug
            }
        return super().to_representation(instance)


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    composition = CompositionSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and ('display' in request.path or 'groups' in request.path or 'search' in request.path):
            return {
                'id': instance.id,
                'image': instance.image.url,
                # 'thumbnail': instance.image.thumbnail_url,
                'name': instance.name,
                'slug': instance.slug,
                'category': {
                    "name": instance.category.name,
                    "slug": instance.category.slug
                },
                'price': instance.price,
                'previous_price': instance.previous_price,
                'aggr_reviews': instance.reviews_aggr,
                'num_reviews': instance.review_set.count(),
                'composition': [
                    {
                        "name": c.name,
                        "percent": c.percentage
                    } for c in instance.composition.all()
                ]
            }
        
        return super().to_representation(instance)


class GroupSerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ProductGroup
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer(many=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(ModelSerializer):
    products = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'date_created', 'products']

    # def create(self, validated_data):
    #     cart_items_data = validated_data.pop('cart_items')
    #     cart = Cart.objects.create(**validated_data)
    #     for cart_item_data in cart_items_data:
    #         CartItem.objects.create(cart=cart, **cart_item_data)
    #     return cart