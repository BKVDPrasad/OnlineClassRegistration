"""ocr URL Configuration

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
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminLoginl),
    path('adminlog/',views.adminlog,name='adminlog'),
    path('newclass/',views.newclass,name='newclass'),
    path('savedb/',views.savedb,name='savedb'),
    path('viewall/',views.viewall,name='viewall'),
    path('update/',views.update,name='update'),
    path('updatedata/',views.updatedata,name='updatedata'),
    path('delete/',views.delete,name='delete'),
    path('some',views.some,name='some'),

    path('student/',views.student,name='student'),
    path('stureg/',views.stureg,name='stureg'),
    path('savestu/',views.savestu,name='savestu'),
    path('stulogin',views.stulogin,name='stulogin'),
    path('logvalidte/',views.logvalidte,name='logvalidte'),
    path('save/',views.save,name='save')
]
