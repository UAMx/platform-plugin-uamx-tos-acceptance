from django import forms
from .models import TermsOfService

class AcceptanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TermsOfService
        exclude = ['']