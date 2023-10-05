from django.contrib import admin
from .models import TermsOfService

class TermsOfServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'accepted')

admin.site.register(TermsOfService, TermsOfServiceAdmin)