"""
uamx_tos_acceptance Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings, PluginContexts
)

class UamxTosAcceptanceConfig(AppConfig):
    """
    Configuration for the uamx_tos_acceptance Django application.
    """

    name = 'uamx_tos_acceptance'

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {

        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {

            # Configure the Plugin URLs for each project type, as needed. The full list of project types for edx-platform is
            # here:
            # https://github.com/openedx/edx-platform/blob/2dc79bcab42dafed2c122eb808cdd5604327c890/openedx/core/djangoapps/plugins/constants.py#L14 .
            # Other IDAs may use different values.
            'lms.djangoapp': {

                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'uamx_tos_acceptance',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'uamx_tos_acceptance'
            }
        }
    }    
