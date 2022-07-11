from payment.api.serializers import EsewaPaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
)

from order.models import Order

class EsewaPaymentCreateAPIView(CreateAPIView):
    serializer_class = EsewaPaymentSerializer

    def perform_create(self,serializer):
        serializer.save(paid_by=self.request.user)


class EsewaPaymentListAPIView(ListAPIView):
    serializer_class = EsewaPaymentSerializer


class EsewaPaymentDataView(APIView):
    def get(self,request):
        user = request.user
        order = Order.objects.get(ordered_by__id=user.id).last()
        context = {
            'order': order.id,
            'total_amount': order.total_amount,
            'delivery_charge': order.delivery_charge
        }

        return Response(context)