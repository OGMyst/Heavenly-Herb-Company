from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    stripe_public_key = 'pk_test_51HPD0FAf1PaReHG9eggRTWtYTEwcMeG8DwPDKVDckA71M4KzbQGeUuU5pQc0RtL43juEp3e0KvTWKZaMNr8OYMJH004mhvS2uM'
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
