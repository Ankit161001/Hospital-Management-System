"""hospital URL Configuration

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
from django.urls import path
from pages.views import home_view, appoint_view, lab_view, bed_view, doctor_view, contactus_view, login_view, register_view, ambulance_view, aboutus_view

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from hospital import settings

urlpatterns = [
    path('', home_view, name = 'home'),
    path('ambulance/', ambulance_view),
    path('contactus/', contactus_view),
    path('aboutus/', aboutus_view),
    path('login/', login_view),
    path('login/register/', register_view),
    path('appoint/', appoint_view),
    path('labtest/', lab_view),
    path('bookbed/', bed_view),
    path('doctors/', doctor_view),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
