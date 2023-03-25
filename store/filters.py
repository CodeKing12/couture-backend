from .models import Product
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = filters.CharFilter(field_name='short_description', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='exact')
    composition = filters.CharFilter(field_name='composition__name', lookup_expr='exact')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    review_count = filters.NumberFilter(field_name="review", lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'composition', 'price']