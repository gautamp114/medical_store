from django.urls import path

from payment.api.views import (
    EsewaPaymentCreateAPIView,
    EsewaPaymentListAPIView,
    EsewaPaymentDataView
)

## esewa
urlpatterns = [
    path('payment-create/',EsewaPaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment-list/',EsewaPaymentListAPIView.as_view(), name='payment_list'),
    path('esewa-payment-data/',EsewaPaymentDataView.as_view(), name='esewa_payment_data'),
]
