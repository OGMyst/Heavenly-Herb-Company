from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserGeneralForm, UserAddressForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form_value = request.POST.get('update-form')
        if form_value == "general-update-form":
            form = UserGeneralForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
        elif form_value == "address-update-form":
            form = UserAddressForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Address updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    allOrders = profile.orders.all()
    orders = allOrders.order_by('date').reverse()[:5]
    addresses = profile.addresses.all().reverse()[:2]

    Generalform = UserGeneralForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'default_phone_number': profile.default_phone_number,
    })

    Addressform = UserAddressForm(initial={
                    'default_street_address1': profile.default_street_address1,
                    'default_street_address2': profile.default_street_address2,
                    'default_town_or_city': profile.default_town_or_city,
                    'default_county': profile.default_county,
                    'default_country': profile.default_country,
                    'default_postcode': profile.default_postcode,
    })

    template = 'profiles/profile.html'
    context = {
        'general_form': Generalform,
        'address_form': Addressform,
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
def edit_address(request, address_id):
    """ Edit an address in the store """

    return render(request)


@login_required
def delete_address(request, address_id):
    """ Delete an address from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be logged in to do that.')
        return redirect(reverse('home'))

    messages.success(request, 'Address deleted!')
    return redirect(reverse('profile'))
