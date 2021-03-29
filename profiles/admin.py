from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'userprofile',
        'full_name',
        'phone_number',
        'address_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'country',
        'postcode',
    )

    ordering = ('userprofile',)


admin.site.register(Address, AddressAdmin)
