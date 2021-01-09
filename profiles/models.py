from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


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
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=254)
    street_address2 = models.CharField(max_length=254)
    town_or_city = models.CharField(max_length=254)
    county = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    postcode = models.CharField(max_length=254)

    def __str__(self):
        return self
