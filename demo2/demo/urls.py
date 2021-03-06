"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^without-injection/$', without_injection, name='without-injection'),
    url('^with-injection/(?P<data>.*)$', with_injection, name='with-injection'),
    url('^with-request-injection/$', with_request_injection, name='with-request-injection'),
    url('^container-inject/$', container_inject, name='container-inject'),
    url('^generic-view/$', GenericView.as_view(), name='generic-view'),
]
