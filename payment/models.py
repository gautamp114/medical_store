from django.db import models
from django.contrib.auth import get_user_model

from order.models import Order

User = get_user_model()

class EsewaPayment(models.Model):
    related_order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="esewa_order")
    paid_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name="esewa_user")
    paid_on = models.DateTimeField(auto_now_add=True)
    paid_amount = models.IntegerField()

    class Meta:
        ordering = ['-paid_on']

    def __str__(self):
        return "{} ({})".format(self.related_order,self.paid_by.username)