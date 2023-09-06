from django.db import models
from django.db.models import Manager


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    add_at = models.DateField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return {self.title}


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'Заказ номер {self.pk} клиента {self.customer}'

