"""DOMS URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    url('new/$', views.new, name='inventory_new'),
    url('edit/(?P<warehouse_id>\d+)/$', views.edit, name='inventory_edit'),
    url('delete/(?P<warehouse_id>\d+)/$', views.delete, name='inventory_delete'),
    url('details/(?P<warehouse_id>\d+)/$', views.detail, name='inventory_detail')
]
