from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from fractions import Fraction

# Define helper functions here.

# Create your models here.
class Product(models.Model):
    WEIGHT_CHOICES = (
        ('28g', '28 Grams'),
        ('1/2lb', '1/2 Pound'),
        ('1/4lb', '1/4 Pound'),
    )

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products/")
    short_description = models.CharField(max_length=160)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    weights = models.CharField(max_length=10, choices=WEIGHT_CHOICES)
    price = models.FloatField()
    previous_price = models.FloatField()
    addons = models.ManyToManyField('Addon')
    effects = models.CharField(max_length=65)
    may_relieve = models.CharField(max_length=150)
    aromas = models.CharField(max_length=50)
    composition = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.weights.count() > 3:
            raise ValidationError(_("You can only select 3 weight values"), code="max_values")
        return super().clean()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Addon(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()

    class Meta:
        verbose_name = "Addon"
        verbose_name_plural = "Addons"


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=650)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# I'm creating the backend, using Django, for an ecommerce store that sells different categories of weed. 