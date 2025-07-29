# Plugin settings.py overrides

# lint-amnesty, pylint: disable=missing-function-docstring, missing-module-docstring
def plugin_settings(settings):

    # Add UAMxTermsOfServiceMiddleware middleware to the list of Django middlewares
    settings.MIDDLEWARE += ['platform_plugin_uamx_tos_acceptance.middleware.UAMxTermsOfServiceMiddleware']