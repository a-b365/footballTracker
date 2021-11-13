"""Projectfootball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
	
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),


]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/',include('rosetta.urls')),
    ]


urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name="homepage.html"), name='home'),
    path('about/',TemplateView.as_view(template_name="info.html"),name='about'),
    path('news/',include('News.urls')),
    path('players/',include('Players.urls')),
    path('assorted/',include('assortedApps.urls')),
    path('search/',views.Search,name='search'),

)
