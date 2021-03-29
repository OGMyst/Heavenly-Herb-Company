import uuid

from django.db import models


class ContactUs(models.Model):
    message_number = models.CharField(max_length=32, null=False,
                                      editable=False)
    user_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254, null=True,
                               blank=True)
    message = models.TextField()

    def _generate_message_number(self):
        """
        Generate a random, unique message number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.message_number
