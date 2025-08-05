from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# USER MODEL
class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('manager', 'Store Manager'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=15)

# PRODUCT MODEL
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    times_bought = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# CART ITEM
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

# WISHLIST ITEM
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# ORDER
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

# ORDER ITEM
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
