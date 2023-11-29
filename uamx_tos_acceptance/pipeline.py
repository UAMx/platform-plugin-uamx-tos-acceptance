from openedx_filters import PipelineStep
from openedx_filters.learning.filters import DashboardRenderStarted

from .models import TermsOfService

class RedirectFromDashboard(PipelineStep):

    def run_filter(self, context, template_name, *args, **kwargs):  # pylint: disable=arguments-differ

        accepted_to = TermsOfService.objects.filter(user=context.get('user'), accepted=True).exists()

        if not accepted_to:
            raise DashboardRenderStarted.RedirectToPage(
                "You must accept terms of service to continue",
                redirect_to="/uamx_tos_acceptance"
            )