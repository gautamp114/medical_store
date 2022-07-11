from django.contrib import admin
from order.models import Order,OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1


class OrderAdmin(admin.ModelAdmin):

    list_display = ("ordered_by", "ordered_on", "payment_through",
                    "total_amount")
    inlines = [
        OrderItemsInline,
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)