from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileGeneralForm, UserProfileAddressForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    Generalform = UserProfileGeneralForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
    })

    Addressform = UserProfileAddressForm(initial={
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
    })

    template = 'profiles/profile.html'
    context = {
        'general_form': Generalform,
        'address_form': Addressform
    }

    return render(request, template, context)
