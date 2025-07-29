"""
URLs for uamx_tos_acceptance.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('uamx_tos_acceptance', views.index, name='index'),
]