"""bestmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from bestmovies import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Telugu/', views.Telugu, name='Telugu'),
    path('English/', views.English, name='English'),
    path('', views.Home, name='Home'),
    path('Animation/', views.Animation, name='Animation'),
    path('Malayalam/', views.Malayalam, name='Malayalam'),
    path('Hindi/', views.Hindi, name='Hindi'),
    path('Korean/', views.Korean, name='Korean'),
    path('Horror/', views.Horror, name='Horror'),
    path('Action/', views.Action, name='Action'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
