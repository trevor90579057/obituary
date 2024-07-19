# obituaries/admin.py
from django.contrib import admin
from .models import Obituary
from .admin_site import custom_admin_site


class ObituaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death',
                    'author', 'submission_date')
    search_fields = ('name', 'author')


custom_admin_site.register(Obituary, ObituaryAdmin)
