from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact_us(request):
    """ A view to return the Contact Us page """
    contact_form = ContactForm()
    template = 'contact_us/contact_us.html'

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_us = contact_form.save(commit=False)
            contact_us.save()
            messages.success(request, 'Thank you for your message.' +
                             ' We will be in touch as soon as we can.')
        else:
            messages.error(request, 'Something went wrong when processing' +
                           ' your message. Please check you have filled in' +
                           ' all the fields and that your email address is' +
                           ' correct')

    context = {
            'contact_form': contact_form
    }

    return render(request, template, context)
