from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Define helper functions here.

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
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=650)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title


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