"""cretue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from user import views as Uservw
from tools import views as Toolsvw
from django.conf.urls import url,include


from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
sta = RedirectView.as_view(url='/static/img/', permanent=True)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Uservw.Index),
    path('favicon.ico', favicon_view),
    path('img/', sta),

    #tools app
    path('tools/', include('tools.urls')),

    #user app
    path('ems/', include('user.urls')),
    path('crawl/', include('user.crawl_urls')),

    #user
    path('signin', Uservw.signin),

    path('login', Uservw.login),
	path('logout', Uservw.loginout),
    
]
