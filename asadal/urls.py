"""asadal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from asadal.landing.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^product/dufflebag/$', ProductDufflebag.as_view()),
    url(r'^product/raincover/$', ProductRaincover.as_view()),
    url(r'^product/tawoobagpack/$', ProductTawoobagpack.as_view()),
    url(r'^product/waistbag/$', ProductWaistbag.as_view()),
    url(r'^product/$', ProductMain.as_view()),
    url(r'^about/$', AboutView.as_view()),
    url(r'^contact/$', ContactView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

