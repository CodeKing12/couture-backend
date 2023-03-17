from django.contrib import admin
from .models import Product, Composition, Addon, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "slug", "price")

admin.site.register(Product, ProductAdmin) 
admin.site.register(Composition)
admin.site.register(Addon)
admin.site.register(Category)