"""BlackBelt URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from apps.loginAndReg.views import index
import apps.wish_list.views
import apps.loginAndReg.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apps.loginAndReg.views.index),
    url(r'^loginAndReg/', include('apps.loginAndReg.urls')),
    url(r'^landingPage/', apps.wish_list.views.landing),
    url(r'^moreInfo/(?P<target>\d+)/$', apps.wish_list.views.productInfo),
    url(r'^addItem/', apps.wish_list.views.addItem),
    url(r'^addProduct/', apps.wish_list.views.addProduct),
    url(r'^delete/(?P<target>\d+)/$', apps.wish_list.views.delete),
    url(r'^addToCurrent/(?P<target>\d+)/$', apps.wish_list.views.addToCurrentUser),
    url(r'^removeFromCurrent/(?P<target>\d+)/$', apps.wish_list.views.removeFromCurrentUser)
]
