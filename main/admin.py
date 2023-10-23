from django.contrib import admin

from .models import Donor, Beneficiary, Help, HelpRequest

# Register your models here.

admin.site.register(Donor)
admin.site.register(Beneficiary)
admin.site.register(Help)
admin.site.register(HelpRequest)