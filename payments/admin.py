from django.contrib import admin
from .models import Fine, FinePayment


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ['member', 'amount']


@admin.register(FinePayment)
class FinePaymentAdmin(admin.ModelAdmin):
    list_display = ["member", "payment_amount", "payment_date"]
