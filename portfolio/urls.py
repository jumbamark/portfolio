"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # referecing the media root file in settings.py
from django.conf.urls.static import static

urlpatterns = [
    path('jumbamark/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# configure the media url
# setting the url path to the media root in settings.py - when we try to render an image create a url path for a specific image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# configure our static files in production - when we are deploying it django is not meant to save staticfiles so we're gonna have to customize
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
