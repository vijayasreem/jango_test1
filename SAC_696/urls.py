from django.urls import path

urlpatterns = [
    path('payment_gateway_integration/', payment_gateway_integration, name='payment_gateway_integration'),
    path('payment_success/', payment_success, name='payment_success'),
    path('payment_fail/', payment_fail, name='payment_fail'),
]