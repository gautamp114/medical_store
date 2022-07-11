from webbrowser import get
from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)


from accounts.api.permissions import IsAllUser

from order.api.serializers import OrderSerializer,StockSerializer
from order.models import Order,Stock


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self,serializer):
        return serializer.save(
            ordered_by=self.request.user
        )

class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAllUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAllUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

##orderitems

# class OrderItemCreateAPIView(CreateAPIView):
#     serializer_class = OrderItemsSerializer

#     # def perform_create(self,serializer):
#     #     return serializer.save(
#     #         OrderItemed_by=self.request.user
#     #     )

# class OrderItemsListAPIView(ListAPIView):
#     serializer_class = OrderItemsSerializer
#     queryset = OrderItems.objects.all()


# class OrderItemUpdateAPIView(UpdateAPIView):
#     permission_classes = [IsAllUser]
#     serializer_class = OrderItemsSerializer
#     queryset = OrderItems.objects.all()


# class OrderItemDeleteAPIView(DestroyAPIView):
#     permission_classes = [IsAllUser]
#     serializer_class = OrderItemsSerializer
#     queryset = OrderItems.objects.all()


## stock
class StockCreateAPIView(CreateAPIView):
    serializer_class = StockSerializer

    def perform_create(self,serializer):
        return serializer.save(
            created_by=self.request.user
        )

class StockListAPIView(ListAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAllUser]
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAllUser]
    serializer_class = StockSerializer
    queryset = Stock.objects.all()