## Single Sign On
  # step 1 :
   
      pip install django-allauth 

# step2:
   In the installed app add these requirements also
   
        INSTALLED_APPS = [
          'allauth',
          'allauth.account',
          'allauth.socialaccount.providers.github',
          'allauth.socialaccount.providers.google',
          'allauth.socialaccount.providers.facebook',
          
      
      ]

        MIDDLEWARE = [
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'allauth.account.middleware.AccountMiddleware',
        ]
         AUTHENTICATION_BACKENDS = [
        
        'django.contrib.auth.backends.ModelBackend',
    
        'allauth.account.auth_backends.AuthenticationBackend',
       
          ]
        SITE_ID=1

     

# step3:
  In urls.py in main app add the given url
  
      urlpatterns = [
              path('admin/', admin.site.urls),
              path('accounts/', include('allauth.urls')),
        
        ]
# step4:

  Run the post command
  
      python manage.py migrate




      
      
          
 
