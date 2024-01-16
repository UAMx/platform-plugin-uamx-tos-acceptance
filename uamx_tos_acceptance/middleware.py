import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers

from .models import TermsOfService

class UAMxTermsOfServiceMiddleware:
    """
    The purppose of this middleware is to check if a user has accepted the 
    Terms Of Service of the application and if not, redirect her 
    to the terms of service acceptance form
    
    So we create this middleware to listen to any request 
    and redirect the user if needed
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Check if user is authenticated
        if request.user.is_authenticated:

            # Check the state of TOS acceptance
            accepted = TermsOfService.objects.filter(user=request.user, accepted=True).exists()

            # Redirect ONLY if user has not accepted the TOS
            if not accepted:

                # catch api login_session response and modify redirect_url
                # to redirect user to TOS
                if request.path == '/api/user/v2/account/login_session/':
                    lms_root_url = configuration_helpers.get_value('LMS_ROOT_URL', settings.LMS_ROOT_URL)
                    parsed = json.loads(response.content.decode('utf-8'))
                    parsed['redirect_url']='{}/uamx_tos_acceptance'.format(lms_root_url)
                    return JsonResponse(parsed, safe=False)

                # While in TOS the menu is still visible, this prevents
                # user from navigate to new page
                should_block_url = any(request.path.startswith(x) for x in ('/learning', '/dashboard', '/courses', '/u/{}'.format(request.user.username), '/account/settings', '/course_mode'))
                if should_block_url:
                    return redirect('/uamx_tos_acceptance')

        return response
