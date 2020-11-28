from django.shortcuts import render

# Create your views here.


def profile(request):
    """ A view to return the index page """

    return render(request, 'profile/profile.html')
