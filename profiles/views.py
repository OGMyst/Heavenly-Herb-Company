from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Address
from .forms import UserAddressForm, AddressForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    allOrders = profile.orders.all()
    orders = allOrders.order_by('date').reverse()[:5]
    addresses = profile.addresses.all().reverse()[:2]

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'addresses': addresses
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def edit_address(request, address_number):
    """ Edit an address from user profile """
    address = get_object_or_404(Address, address_number=address_number)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    address_form = AddressForm(initial={
        'full_name': address.full_name,
        'street_address1': address.street_address1,
        'street_address2': address.street_address2,
        'town_or_city': address.town_or_city,
        'county': address.county,
        'country': address.country,
        'postcode': address.postcode,
        'phone_number': address.phone_number,
    })

    template = 'profiles/edit_address.html'
    context = {
        'address_form': address_form,
        'address': address
    }

    return render(request, template, context)


@login_required
def delete_address(request, address_id):
    """ Delete an address from user profile """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be logged in to do that.')
        return redirect(reverse('home'))

    messages.success(request, 'Address deleted!')
    return redirect(reverse('profile'))
