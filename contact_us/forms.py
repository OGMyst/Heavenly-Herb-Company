from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        labels = {"user_email": "Your Email Address"}
        fields = ('user_email',
                  'subject',
                  'message',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'