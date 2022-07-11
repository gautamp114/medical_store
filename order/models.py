from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from product.models import Product

User = get_user_model()


PAYMENT_METHOD = (
    ('0','Esewa'),
    ('1','Cash On Delivery'),
)


class Order(models.Model):
    ordered_by = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name="order_user")
    ordered_on = models.DateTimeField(auto_now_add=True)
    payment_through = models.CharField(max_length=50,choices=PAYMENT_METHOD,default=0)
    total_amount = models.PositiveIntegerField(default=0)
    delivery_charge = models.PositiveIntegerField(default=50)

    class Meta:
        ordering = ['-ordered_on']

    def __str__(self):
        return '{} ({})'.format(self.id,self.ordered_by.username)


class OrderItems(models.Model):
    related_order = models.ForeignKey(
        Order,on_delete=models.CASCADE,related_name="orderitems_order")
    related_product = models.ForeignKey(
        Product,related_name="orderitems_product",on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} ({})'.format(self.related_order.ordered_by.username,self.related_product.name)


class Stock(models.Model):
    related_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="stock_product")
    quantity = models.PositiveIntegerField(null=False, default=0)
    available_quantity = models.PositiveIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="stock_created_by", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.product.name