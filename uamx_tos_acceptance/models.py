"""
Database models for uamx_tos_acceptance.
"""
# from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db import models


class TermsOfService(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='terms_of_service')
    accepted = models.BooleanField('Acepto los términos y condiciones', default=False)

    def __str__(self):
        return 'TermsOfService id'.format(self.id)
