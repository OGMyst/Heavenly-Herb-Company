from django.contrib import admin
from .models import ContactUs
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'user_email',
        'subject',
        'message',
    )
    actions = ["Resolved"]


admin.site.register(ContactUs, ContactUsAdmin)
