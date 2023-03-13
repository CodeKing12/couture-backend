from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from fractions import Fraction

# Define helper functions here.

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products/")
    short_description = models.CharField(max_length=160)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    weights = models.ManyToManyField('Weight')
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


class Weight(models.Model):
    WEIGHT_CHOICES = (
        ('g', 'Gram'),
        ('oz', 'Ounce (28 grams)'),
        ('lb', 'Pound (16 ounces)'),
    )

    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    unit = models.CharField(max_length=20, choices=WEIGHT_CHOICES)

    def as_fraction(self):
        fraction_form = Fraction(self.quantity).limit_denominator()
        if fraction_form.denominator == 1:
            the_fraction = fraction_form.numerator
        elif fraction_form.numerator > fraction_form.denominator:
            whole_num = int(fraction_form.numerator / fraction_form.denominator)
            mixed_fraction = str(fraction_form.numerator % fraction_form.denominator) + "/" + str(fraction_form.denominator)
            the_fraction = f"{whole_num} {mixed_fraction}"
        else:
            the_fraction = str(fraction_form.numerator) + "/" + str(fraction_form.denominator)
            
        return the_fraction
    # Which of the following is the best way to represent the following data in an admin interface: '4 1/2lb', '4 1/2 lb' or any way you can come up with

    def __str__(self):
        return self.as_fraction() + self.unit

    class Meta:
        verbose_name = "Weight"
        verbose_name_plural = "Weights"


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