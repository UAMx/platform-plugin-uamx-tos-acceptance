"""
URLs for platform_plugin_uamx_tos_acceptance.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('platform_plugin_uamx_tos_acceptance', views.index, name='index'),
]