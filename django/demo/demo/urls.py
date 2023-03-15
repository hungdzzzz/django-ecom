"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
import django
from django.contrib import admin

from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
urlpatterns = [

    #errors page
    path('404',views.Error404,name='404') ,  

    path('about',views.About,name='about'),
    path('contact',views.Contact,name='contact'),
    path('products',views.Products,name='products'),

    path('product/filter-data',views.filter_data,name="filter-data"),

    path('admin/', admin.site.urls),
    path('master/',views.Master,name='master'),
    path('main/',views.HOME,name='home'),
    path('product/<slug:slug>',views.PRODUCT_DETAILS,name='product_detail'),
#login
    path('account/my-account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.Register,name='handleregister'),
    path('account/profile',views.Profile,name='profile'),
    path('account/login',views.Login,name='handlelogin'),
    path('account/profile/update',views.Profile_UPDATE,name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 

