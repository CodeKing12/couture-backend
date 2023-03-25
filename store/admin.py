from django.contrib import admin
from .models import Product, Composition, Addon, Category, ProductGroup, Review

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'price', 'reviews_aggr')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Product, ProductAdmin) 
admin.site.register(Composition)
admin.site.register(Addon)
admin.site.register(ProductGroup)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)