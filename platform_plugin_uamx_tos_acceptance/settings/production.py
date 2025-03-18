# Plugin settings.py overrides

from os.path import abspath, dirname, join

from platform_plugin_uamx_tos_acceptance import ROOT_DIRECTORY


INSTALLED_APPS = [
    "platform_plugin_uamx_tos_acceptance",
]

# lint-amnesty, pylint: disable=missing-function-docstring, missing-module-docstring
def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    # Add UAMxTermsOfServiceMiddleware middleware to the list of Django middlewares
    settings.MIDDLEWARE += ['platform_plugin_uamx_tos_acceptance.middleware.UAMxTermsOfServiceMiddleware']