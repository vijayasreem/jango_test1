from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PaymentForm

def payment_gateway_integration(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            if payment_method == 'credit_debit':
                # Implement credit/debit card payment mechanism
                return redirect('payment_success')
            elif payment_method == 'paypal':
                # Implement PayPal payment mechanism
                return redirect('payment_success')
            elif payment_method == 'stripe':
                # Implement Stripe payment mechanism
                return redirect('payment_success')
            else:
                messages.error(request, 'Invalid payment method')
                return redirect('payment_fail')
        else:
            return redirect('payment_fail')
    else:
        form = PaymentForm()
    return render(request, 'payment_gateway_integration.html', {'form': form})

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_fail(request):
    return render(request, 'payment_fail.html')