from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "slug", "price")

admin.site.register(Product, ProductAdmin) 
admin.site.register(Ingredient)
admin.site.register(Addon)
admin.site.register(Category)