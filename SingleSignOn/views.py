from django.shortcuts import render

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import SSOProfile

class SSOBackend(BaseBackend):
    def authenticate(self, request, external_id=None, sso_provider=None, **kwargs):
        try:
            sso_profile = SSOProfile.objects.get(external_id=external_id, sso_provider=sso_provider)
            return sso_profile.user
        except SSOProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

