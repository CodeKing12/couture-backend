from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email:
            return ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_apiuser', True)
        extra_fields.setdefault('is_vendor', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff set to True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser set to True.'))
        if extra_fields.get('is_apiuser') is not True:
            raise ValueError(('Superuser must have is_apiuser set to True.'))
        if extra_fields.get('is_vendor') is not True:
            raise ValueError(('Superuser must have is_vendor set to True.'))

        return self.create_user(first_name=first_name, last_name=last_name, email=email, password=password, **extra_fields)
    
# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# class AddressBook(models.Model):
#     address = models.CharField(max_length=250)

class Account(AbstractUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_apiuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    def get_full_name(self):
        return "%s %s"%(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

