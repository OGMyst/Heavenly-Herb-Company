from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileGeneralForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    Generalform = UserProfileGeneralForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'general_form': Generalform,
    }

    return render(request, template, context)
