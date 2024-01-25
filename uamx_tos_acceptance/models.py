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
        accepted_tos (Boolean): The state of the TOS acceptance by the user. True if accepted, False if not.
        accepted_privacy (Boolean): The state of the privacy policy acceptance by the user. True if accepted, False if not.
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='terms_of_service')
    accepted_tos = models.BooleanField('Acepto los términos y condiciones', default=False)
    accepted_privacy = models.BooleanField('Acepto la política de privacidad', default=False)

    @property
    def is_accepted(self):
        return self.accepted_tos and self.accepted_privacy

    def __str__(self):
        return 'TermsOfService id'.format(self.id)
