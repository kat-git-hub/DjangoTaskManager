from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin


class CustomAccessMixin(AccessMixin):
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')
