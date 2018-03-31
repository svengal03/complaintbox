"""complaintbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Exampledjango.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url,include
from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('complaint.urls')),
    url(r'^$',home),
]
