from order.models import Order, OrderItems, Stock
from rest_framework import serializers

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('related_product','quantity')


class OrderSerializer(serializers.ModelSerializer):
    orderitems_order = OrderItemsSerializer(many=True,required=True)
    class Meta:
        model = Order
        fields = ('orderitems_order','payment_through','total_amount','delivery_charge')

    def create(self, validated_data):
        order_items_data = validated_data.pop('orderitems_order')
        order = Order.objects.create(**validated_data)
        for data in order_items_data:
            OrderItems.objects.create(related_order=order,**data)
        return order


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('related_product','quantity','available_quantity')