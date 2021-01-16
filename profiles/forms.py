from django import forms
from .models import UserProfile, Address


class UserGeneralForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('full_name',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'country',
                  'postcode',
                  'phone_number',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'country': 'Country',
            'postcode': 'Postal Code',
            'phone_number': 'Phone Number',
        }

        # self.fields['street_address_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
