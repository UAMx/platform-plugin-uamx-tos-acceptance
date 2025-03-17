import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from django.contrib.auth import logout

from .models import TermsOfService

class UAMxTermsOfServiceMiddleware:
    """
    The purppose of this middleware is to check if a user has accepted the 
    Terms Of Service of the application and if not, redirect her 
    to the terms of service acceptance form.
    
    So we create this middleware to listen to any request 
    and redirect the user if needed.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if request.user.is_authenticated:
            
            # if user is authenticated,
            # check the state of TOS acceptance 
            is_accepted = TermsOfService.objects.filter(user=request.user, accepted_tos=True, accepted_privacy=True, ).exists()
            lms_root_url = configuration_helpers.get_value('LMS_ROOT_URL', settings.LMS_ROOT_URL)

            # Redirect ONLY if user has not accepted the TOS
            if not is_accepted:
                
                # catch api login_session response and modify redirect_url
                # to redirect user to TOS
                if request.path == '/api/user/v2/account/login_session/':
                    payload = response.content.decode('utf-8')

                    if isinstance(payload, str):
                        parsed = json.loads(payload)
                        parsed['redirect_url']='{}/platform_plugin_uamx_tos_acceptance'.format(lms_root_url)
                        response = JsonResponse(parsed, safe=False)

                # While in TOS the menu is still visible, this prevents
                # user from navigate to new page
                should_redirect = any(request.path.startswith(x) for x in ('/dashboard', '/courses', '/u/{}'.format(request.user.username), '/account/settings', '/course_mode'))
                if should_redirect:
                    response = redirect('/platform_plugin_uamx_tos_acceptance')
                
                # As we cannot redirect users under an MFE, we just log them out 
                # and try to redirect them to the home page
                # WARNING: This will eventually not work at the first time a user
                # tries to navigate through a course, but as he/she is logged out 
                # eventually it will find the need to relogin
                should_logout = any(request.path.startswith(x) for x in ('/xblock', '/courses/course', '/api/course_home', '/api/user_tours'))
                if should_logout:
                    logout(request)
                    response = redirect('{}/logout'.format(lms_root_url))

        else:

            # Prevent redirect to MFEs when a user is not logged in
            # To do so we change the "welcomePageRedirectUrl" inside 
            # "contextData" dictionary for the /api/mfe_context, an API 
            # that is used to manage user status for MFE's
            if request.path.startswith('/api/mfe_context'):
                payload = response.content.decode('utf-8')
                parsed = json.loads(response.content)
                parsed['contextData']['welcomePageRedirectUrl'] = '/dashboard'
                response = JsonResponse(parsed, safe=False)

        return response
