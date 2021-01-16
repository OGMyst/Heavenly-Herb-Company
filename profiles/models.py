from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

import uuid


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(default='', max_length=50, null=False, blank=False)
    email = models.EmailField(default='', max_length=254, null=False, blank=False)
    phone_number = models.CharField(default='', max_length=20, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Address(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                    null=True, blank=True, editable=False,
                                    related_name="addresses")
    address_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(default='', max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=254)
    street_address2 = models.CharField(max_length=254)
    town_or_city = models.CharField(max_length=254)
    county = models.CharField(max_length=254)
    country = CountryField(blank_label="Country *",default = 'UK', null=False, blank=False)
    postcode = models.CharField(max_length=254)
    phone_number = models.CharField(default='', max_length=20, null=False, blank=False)

    def _generate_address_number(self):
        """
        Generate a random, unique address number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the address number
        if it hasn't been set already.
        """
        if not self.address_number:
            self.address_number = self._generate_address_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.street_address1
