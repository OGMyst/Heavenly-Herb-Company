from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileGeneralForm(forms.ModelForm):
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
            'full_name': User.username,
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
