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
from reservation import views as reservationviews




urlpatterns = [
    path('home/', include('home.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('car/', include('car.urls')),
    path('category/<int:id>/<slug:slug>/',  views.category_cars ,name='category_cars'),
    path('car/<int:id>/<slug:slug>/',  views.car_detail,name='car_detail'),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('search/', views.car_search, name='car_search'),
    path('search_auto/', views.car_search_auto, name='car_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('join/', views.join_view, name='join_view'),
    path('user/', include('user.urls')),
    path('shopcart/', include('reservation.urls')),
    path('reservation/', reservationviews.shopcart, name='reservation'),
    path('faq/', views.faq, name='faq'),


]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)