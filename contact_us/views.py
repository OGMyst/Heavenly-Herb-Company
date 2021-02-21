from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def contact_us(request):
    """ A view to return the Contact Us page """

    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                email_sent = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/', email_sent)

    return render(request, 'contact_us/contact_us.html', {'contact_form': contact_form})
