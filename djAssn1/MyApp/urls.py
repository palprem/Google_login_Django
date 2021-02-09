from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
app_name='MyApp'

urlpatterns = [
    
    path("login", views.login),
    path("index", views.index),
    path("img", views.img),
    path("dp", views.dp),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)