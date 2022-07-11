from django.urls import path

from order.api.views import (
    OrderCreateAPIView,
    OrderListAPIView,
    OrderUpdateAPIView,
    OrderDeleteAPIView,

    StockCreateAPIView,
    StockListAPIView,
    StockUpdateAPIView,
    StockDeleteAPIView,
)

## order
urlpatterns = [
    path('order-create/',OrderCreateAPIView.as_view(), name='order_create'),
    path('order-list/',OrderListAPIView.as_view(), name='order_list'),
    path('order-update/<int:pk>/',OrderUpdateAPIView.as_view(), name='order_update'),
    path('order-delete/<int:pk>/',OrderDeleteAPIView.as_view(), name='order_delete'),
]

## stock
urlpatterns = urlpatterns + [
    path('stock-create/',StockCreateAPIView.as_view(), name='stock_create'),
    path('stock-list/',StockListAPIView.as_view(), name='stock_list'),
    path('stock-update/<int:pk>/',StockUpdateAPIView.as_view(), name='stock_update'),
    path('stock-delete/<int:pk>/',StockDeleteAPIView.as_view(), name='stock_delete'),
]
     
