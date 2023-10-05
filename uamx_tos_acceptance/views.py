from django.shortcuts import render, redirect
from django.forms import HiddenInput

from .forms import AcceptanceForm
from .models import TermsOfService

from common.djangoapps.edxmako.shortcuts import render_to_response

def index(request):

    if request.user.is_authenticated:

        instance, created = TermsOfService.objects.get_or_create(user=request.user)

        if instance.accepted:
            return redirect('/dashboard')

        form = AcceptanceForm(instance=instance)

        if request.POST:
            
            form = AcceptanceForm(request.POST, instance=instance)

            if form.is_valid():
                    tos = form.save()
                    return redirect('/dashboard')

        form.fields['user'].widget = HiddenInput()
        return render_to_response('uamx_tos_acceptance/index.html', {'form': form})

    else:
        return redirect('accounts/login')