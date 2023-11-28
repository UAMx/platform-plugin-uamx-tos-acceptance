from openedx_filters import PipelineStep
from openedx_filters.learning.filters import StudentLoginRequested

from .models import TermsOfService

class StopLogin(PipelineStep):
    """
    Based on https://github.com/eduNEXT/openedx-filters-samples/blob/c22cf063ccc82b862310b8dae45731ecb3abdd73/openedx_filters_samples/samples/pipeline.py#L292

    Stop login process raising PreventLogin exception when user has not accepted terms of service and redirect user to uamx_tos_acceptance
    """

    def run_filter(self, user, *args, **kwargs):  # pylint: disable=arguments-differ

        tos_instance = TermsOfService.objects.filter(user=user, accepted=True)

        if tos_instance.exists():
            return {}
            
        raise StudentLoginRequested.PreventLogin(
            "You must accept Terms of service.", redirect_to="/uamx_tos_acceptance", error_code="pre-register-login-forbidden"
        )