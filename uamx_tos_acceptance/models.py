"""
Database models for uamx_tos_acceptance.
"""
# from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db import models


class TermsOfService(TimeStampedModel):
    """
    Model to keep track of the terms of service acceptance by the users

    Variables:
        user (ForeignKey): The user that will accept (or not) the TOS
        accepted (Boolean): The state of the TOS accepntance by the user. True if accepted, False if not.
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='terms_of_service')
    accepted = models.BooleanField('Acepto los términos y condiciones', default=False)

    def __str__(self):
        return 'TermsOfService id'.format(self.id)
