from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
from django.db.models import CharField


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self) -> CharField:
        return self.description


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1, message="Weka sawa apa wewe...")]
                                )
    inventory = models.IntegerField()
    slug = models.CharField(max_length=200, null=True)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # promotions = models.ManyToManyField(Promotion, related_name='product')
    promotions = models.ManyToManyField(Promotion, related_name='product', blank=True)

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        ordering = ['title']


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'

    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'BRONZE'),
        (MEMBERSHIP_GOLD, 'GOLD'),
        (MEMBERSHIP_SILVER, 'SILVER'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE, max_length=200)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self) -> str:
        fullname = f"{self.first_name} {self.last_name}"
        return fullname


class Meta:
    db_table = 'store_customers'
    indexes = [
        models.Index(fields=['email', 'first_name', 'email', 'last_name'])
    ]


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('P', 'pending'),
        ('C', 'complete'),
        ('F', 'fail')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_CHOICES, default='p')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self) -> str:
        datePlaced = str(self.placed_at)
        return datePlaced


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


#
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        valueOut = f"{self.order.placed_at} {self.product.title}"
        return valueOut


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
