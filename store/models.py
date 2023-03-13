from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products/")
    short_description = models.CharField(max_length=160)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    weights = models.JSONField()
    price = models.FloatField()
    previous_price = models.FloatField()
    addons = models.ManyToManyField('Addon')
    effects = models.CharField(max_length=65)
    may_relieve = models.CharField(max_length=150)
    aromas = models.CharField(max_length=50)
    composition = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

class Addon(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=650)

# I'm creating the backend, using Django, for an ecommerce store that sells different categories of weed. 