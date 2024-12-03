from django.contrib import admin

from django.contrib import admin
from .models import SSOProfile, SSOProvider

@admin.register(SSOProvider)
class SSOProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_id', 'redirect_uri')  
    search_fields = ('name', 'client_id')  
    ordering = ('name',)  
    list_filter = ('scopes',) 

@admin.register(SSOProfile)
class SSOProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sso_provider', 'external_id', 'created_at', 'updated_at')  
    search_fields = ('user__username', 'sso_provider', 'external_id') 
    ordering = ('user', 'sso_provider') 
    list_filter = ('sso_provider',)  

