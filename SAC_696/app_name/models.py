# models.py

from django.db import models

class PaymentGateway(models.Model):
    payment_method = models.CharField(max_length=255)
    payment_details = models.TextField()
    redirect_url = models.URLField()
    payment_status = models.CharField(max_length=255)
    payment_log = models.TextField()

class PaymentTransaction(models.Model):
    payment_gateway = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE)
    payment_result = models.CharField(max_length=255)
    payment_message = models.TextField()
    payment_date = models.DateTimeField(auto_now_add=True)