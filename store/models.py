from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone

# Define helper functions and classes here.

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    image = models.ImageField(upload_to="products/")
    slug = models.SlugField(max_length=250, auto_created=True)
    short_description = models.CharField(max_length=350)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField()
    previous_price = models.FloatField()
    effects = models.CharField(max_length=100)
    may_relieve = models.CharField(max_length=150)
    aromas = models.CharField(max_length=50)
    composition = models.ManyToManyField('Composition')
    reviews_aggr = models.FloatField(auto_created=True, null=True, default=0)

    def save(self, *args, **kwargs): 
        # Change the name of the image only if the object instance is new (i.e. it has not yet created a primary key)
        if not self.pk:
            self.image.name = self.name.lower().replace(" ", "-").strip()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Composition(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Addon(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()

    class Meta:
        verbose_name = "Addon"
        verbose_name_plural = "Addons"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(max_length=70, auto_created=True)
    description = models.TextField(max_length=650)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField("Product")

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review = models.CharField(max_length=250)
    user = models.ForeignKey('authentication.Account', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, auto_created=True)

    def __str__(self):
        return self.product.name

    
@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_review_aggregate(sender, instance, **kwargs):
    total = 0
    for review in instance.product.review_set.all():
        total += review.stars
    try:
        instance.product.reviews_aggr = round(total / instance.product.review_set.count(), 1)
    except ZeroDivisionError:
        instance.product.reviews_aggr = 0
    instance.product.save()

# I'm creating the backend, using Django, for an ecommerce store that sells different categories of weed. 

# WEIGHT_CHOICES = (
#     ('28g', '28 Grams'),
#     ('1/2lb', '1/2 Pound'),
#     ('1/4lb', '1/4 Pound'),
# )

# weights = models.CharField(max_length=10, choices=WEIGHT_CHOICES)
# addons = models.ManyToManyField('Addon')

 # Addons and Weights are for the Cart Model, not for the Product model

# def save(self, *args, **kwargs):
#     if self.weights.count() > 3:
#         raise ValidationError(_("You can only select 3 weight values"), code="max_values")
#     return super().clean()