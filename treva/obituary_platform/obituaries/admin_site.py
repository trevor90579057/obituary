# obituaries/admin_site.py
from django.contrib.admin.sites import AdminSite
from django.shortcuts import redirect
from django.urls import reverse

class CustomAdminSite(AdminSite):
    def login(self, request, extra_context=None):
        response = super().login(request, extra_context)
        if request.user.is_authenticated:
            # Redirect to homepage after login
            return redirect(reverse('homepage'))
        return response

custom_admin_site = CustomAdminSite(name='custom_admin')
