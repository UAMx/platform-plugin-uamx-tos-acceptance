from django.shortcuts import redirect
from django.forms import HiddenInput
from django.contrib.auth.decorators import login_required

from .forms import AcceptanceForm
from .models import TermsOfService

from common.djangoapps.edxmako.shortcuts import render_to_response

@login_required
def index(request):

    # Create or retrive TermsOfService instance for the logged user
    instance, created = TermsOfService.objects.get_or_create(user=request.user)

    # If TOS are already accepted, redirect to dashboard
    # TODO: redirect to wherever the user was going to
    if instance.accepted:
        return redirect('/dashboard')

    # Create an AcceptanceForm with the provided instance
    form = AcceptanceForm(instance=instance)

    if request.POST:

        # Fill up the form with the data provided in POST
        form = AcceptanceForm(request.POST, instance=instance)

        # Validate form data and if everything OK redirect to dashboard
        if form.is_valid():
                tos = form.save()
                return redirect('/dashboard')

    # We should hide the user field as it is not relevant for the user
    # and he/she should not modify it
    form.fields['user'].widget = HiddenInput()
    
    return render_to_response('uamx_tos_acceptance/index.html', {'form': form})
