# Plugin settings.py overrides

from collections import OrderedDict
from django.apps import apps

# lint-amnesty, pylint: disable=missing-function-docstring, missing-module-docstring
def plugin_settings(settings):

    settings.INSTALLED_APPS += ("platform_plugin_uamx_tos_acceptance", )
    # To load the new app let's reset app_configs, the dictionary
    # with the configuration of loaded apps
    apps.app_configs = OrderedDict()
    # set ready to false so that populate will work 
    apps.ready = False
    # re-initialize them all; is there a way to add just one without reloading them all?
    apps.populate(settings.INSTALLED_APPS)

    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    # Add UAMxTermsOfServiceMiddleware middleware to the list of Django middlewares
    settings.MIDDLEWARE += ['platform_plugin_uamx_tos_acceptance.middleware.UAMxTermsOfServiceMiddleware']