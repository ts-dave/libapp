from django.db import models
from library.models import Member, Loan


class Fine(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,
                               related_name='fines')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE,
                             related_name="fines")
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)


class FinePayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,
                               related_name='payments')
    fine = models.ForeignKey(Fine, on_delete=models.SET_NULL,
                             related_name="payments", null=True)
    payment_date = models.DateTimeField(auto_now=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
