from django.db import models

# Create your models here.
class Dp(models.Model):
     dp = models.ImageField(upload_to="MyApp/static/",null=True, blank=True)
class Profile(models.Model):
     profile = models.ImageField(upload_to="MyApp/static1/",null=True, blank=True)
