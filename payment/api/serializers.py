from payment.models import EsewaPayment
from rest_framework import serializers

from order.models import Order

class EsewaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsewaPayment
        fields = ('paid_amount')

    def create(self, validated_data):
        user = self.request.user
        order = Order.objects.get(ordered_by__id=user.id).last()
        return order
