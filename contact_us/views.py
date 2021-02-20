from django.shortcuts import render

# Create your views here.


def contact_us(request):
    """ A view to return the Contact Us page """

    return render(request, 'contact_us/contact_us.html')