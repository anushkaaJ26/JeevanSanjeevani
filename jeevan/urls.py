"""jeevan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('signin/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/profile/',views.profile,name='profile'),
    path('dashboard/profile1/',views.profile1,name='profile1'),
    path('dashboard/profile2/',views.profile2,name='profile2'),
    path('dashboard/profile3/',views.profile3,name='profile3'),
    path('dashboard/profile/aadhaar',views.aadhaar,name='aadhaar'),
    path('dashboard/profile/license',views.license,name='license'),
    path('dashboard/profile/report',views.report,name='report'),
    # path('dashboard/profileNext/report1',views.report1,name='report1'),
    # path('dashboard/profileNext/license1',views.license1,name='license1'),
    # path('dashboard/profileNext/aadhaar1',views.aadhaar1,name='aadhaar1'),

]
