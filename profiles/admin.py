from django.contrib import admin

from .models import Address
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'userprofile',
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
