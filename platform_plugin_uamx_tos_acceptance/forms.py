from django import forms
from .models import TermsOfService

class AcceptanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        for field_name in self.fields:
            # Adding required attribute to the checkbox 
            # forces the user to check the checkbox before form submition
            self.fields[field_name].widget.attrs.update({'required': 'required'})
            
    class Meta:
        model = TermsOfService
        exclude = ['']
