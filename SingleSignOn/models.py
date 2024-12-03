from django.db import models
from django.contrib.auth.models import SingleSignOn
class SSOProvider(models.Model):
    name = models.CharField(max_length=100)  
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    auth_endpoint = models.URLField()  
    token_endpoint = models.URLField()  
    user_info_endpoint = models.URLField(blank=True, null=True)  
    redirect_uri = models.URLField()  
    scopes = models.TextField(default="openid email profile")  

    def __str__(self):
        return self.name


class SSOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sso_profile')
    sso_provider = models.CharField(max_length=100)  
    external_id = models.CharField(max_length=255, unique=True)  
    access_token = models.TextField(blank=True, null=True)  
    refresh_token = models.TextField(blank=True, null=True) 
    token_expiry = models.DateTimeField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SSO Profile for {self.user.username}"


