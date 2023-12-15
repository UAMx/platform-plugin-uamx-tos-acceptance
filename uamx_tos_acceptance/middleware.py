from django.shortcuts import redirect

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

        # Check if user is uthenticated
        if request.user.is_authenticated:

            # Check the state of TOS acceptance
            accepted = TermsOfService.objects.filter(user=request.user, accepted=True).exists()
            
            # permitted_urls = any(request.path.startswith(x) for x in ('/uamx_tos_acceptance', '/authn', '/api', '/tos', '/admin', '/account'))
            should_block_url = any(request.path.startswith(x) for x in ('/learning', '/dashboard', '/courses', '/u/{}'.format(request.user.username), '/account/settings', '/course_modes'))

            # Redirect ONLY if user has not accepted the TOS
            if not accepted and should_block_url:
                return redirect('/uamx_tos_acceptance')
            
        return response