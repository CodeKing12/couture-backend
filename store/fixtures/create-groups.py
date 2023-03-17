from store.models import Product, ProductGroup
import random

# all_products = list(Product.objects.all().values_list('id', flat=True))
all_products = list(range(50))

best_seller_products = random.sample(all_products, 9)
all_products = [x for x in all_products if x not in best_seller_products]

promotion_products = random.sample(all_products, 9)
all_products = [x for x in all_products if x not in promotion_products]

on_sale_products = random.sample(all_products, 9)
all_products = [x for x in all_products if x not in on_sale_products]

best_seller = ProductGroup.objects.create(name="best-sellers")
promotions = ProductGroup.objects.create(name="promotions")
on_sale = ProductGroup.objects.create(name="on-sale")

best_seller.products.set(Product.objects.filter(id__in=best_seller_products))
promotions.products.set(Product.objects.filter(id__in=promotion_products))
on_sale.products.set(Product.objects.filter(id__in=on_sale_products))