from openedx_filters import PipelineStep
from openedx_filters.learning.filters import DashboardRenderStarted, StudentLoginRequested

from .models import TermsOfService

class RedirectFromDashboard(PipelineStep):

    def run_filter(self, context, template_name, *args, **kwargs):  # pylint: disable=arguments-differ

        accepted_to = TermsOfService.objects.filter(user=context.get('user'), accepted=True).exists()

        print('************')
        print('************')
        print('************')
        print(accepted_to)
        print('************')
        print('************')
        print('************')


        if not accepted_to:
            raise DashboardRenderStarted.RedirectToPage(
                "You must accept terms of service to continue",
                redirect_to="/uamx_tos_acceptance"
            )
        
class StopLogin(PipelineStep):
    """
    Add previous_login field to the user's profile.

    Example usage:

    Add the following configurations to your configuration file:

        "OPEN_EDX_FILTERS_CONFIG": {
            "org.openedx.learning.student.login.requested.v1": {
                "fail_silently": false,
                "pipeline": [
                    "openedx_filters_samples.samples.pipeline.ModifyUserProfileBeforeLogin"
                ]
            }
        }
    """
    def run_filter(self, user, *args, **kwargs):  # pylint: disable=arguments-differ

        # user.profile.set_meta({"previous_login": str(user.last_login)})
        # user.profile.save()
        # return {"user": user}
    
        accepted_to = TermsOfService.objects.filter(user=user, accepted=True).exists()
        

        print('################')
        print('################')
        print('################')
        print(accepted_to)
        print('################')
        print('################')
        print('################')

        if not accepted_to:
            raise StudentLoginRequested.PreventLogin(
                "You must accept terms of service to continue",
                redirect_to="/uamx_tos_acceptance"
            )