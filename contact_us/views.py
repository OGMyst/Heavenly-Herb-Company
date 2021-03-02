from django.shortcuts import render, redirect, reverse

from .forms import ContactForm


def contact_us(request):
    """ A view to return the Contact Us page """
    contact_form = ContactForm()
    template = 'contact_us/contact_us.html'
    context = {
            'contact_form': contact_form
    }

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_us = contact_form.save(commit=False)
            contact_us.save()
            context = {
                "message_saved": True
            }
        else:
            context = {
                "message_saved": True
            }

    return render(request, template, context)
