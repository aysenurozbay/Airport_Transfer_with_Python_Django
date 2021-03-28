"""transfer_project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from home import views

urlpatterns = [
    path('home/', include('home.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('car/', include('car.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)