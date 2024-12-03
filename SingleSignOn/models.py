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


