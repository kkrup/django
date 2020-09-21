import uuid

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(min_length=5, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password_hash = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    public_id = models.CharField(max_length=36, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=180)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(models.Model, self).__init__(self, *args, **kwargs)
        self.public_id = str(uuid.uuid4())


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete='CASCADE')
    count = models.PositiveIntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete='CASCADE')
    count = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField()
