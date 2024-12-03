from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.core.validators import RegexValidator

# user manager sınıfı
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        return self.create_user(email, password, **extra_fields)

# Konum modeli
class Geo(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Lat: {self.lat}, Lng: {self.lng}"
    
    
# Adres Modeli
class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo = models.ForeignKey(Geo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Addresses"
    
    
# Company modeli
class Company(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"
    

# User modeli
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r"^\+\d{2,3} \d{3} \d{3} \d{2} \d{2}$",
        message="Phone number must be entered in the format: +90 555 555 55 55"
    )
    website_regex = RegexValidator(
        regex=r'^(https?://)?(www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]{2,}\.[a-zA-Z]{2,}(?:/.*)?$',
        message="Enter a valid website URL."
    )
    
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)    
    phone = models.CharField(validators=[phone_regex], max_length=18)
    website = models.URLField(validators=[website_regex], default="")
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return f"{self.email}"