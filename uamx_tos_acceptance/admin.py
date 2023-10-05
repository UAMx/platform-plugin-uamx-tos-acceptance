from django.contrib import admin
from .models import TermsOfService

class TermsOfServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('user', 'accepted', 'created', 'modified')

admin.site.register(TermsOfService, TermsOfServiceAdmin)
