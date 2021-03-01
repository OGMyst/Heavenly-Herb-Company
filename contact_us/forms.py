from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Your Email", required=True,
                                  widget=forms.TextInput(
                                    attrs={'class': 'stripe-style-input'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(
                              attrs={'class': 'stripe-style-input'}))
    message = forms.CharField(required=True, widget=forms.Textarea(
                              attrs={'class': 'stripe-style-input'}))
