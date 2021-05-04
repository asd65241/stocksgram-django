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
    url('cats/', views.index_cat, name='product_cat'),
    url('cat/new/$', views.new_cat, name='product_cat_new'),
    url('cat/edit/(?P<cat_id>\d+)/$', views.edit_cat, name='product_cat_edit'),
    url('cat/detail/(?P<cat_id>\d+)/$',views.cat_detail, name='product_cat_detail'),
    url('cat/delete/(?P<product_id>\d+)/$', views.delete_cat, name='product_cat_delete'),
    url('brands/', views.index_brand, name='product_brand'),
    url('brand/new/$', views.new_brand, name='product_brand_new'),
    url('brand/edit/(?P<brand_id>\d+)/$', views.edit_brand, name='product_brand_edit'),
    url('brand/detail/(?P<brand_id>\d+)/$',views.brand_detail, name='product_brand_detail'),
    url('brand/delete/(?P<product_id>\d+)/$', views.delete_brand, name='product_brand_delete'),
    url('new/$', views.new, name='product_new'),
    url('edit/(?P<product_id>\d+)/$', views.edit, name='product_edit'),
    url('detail/(?P<product_id>\d+)/$', views.detail, name='product_detail'),
    url('delete/(?P<product_id>\d+)/$', views.delete_product, name='product_delete'),
    url('addstock/(?P<product_id>\d+)/$', views.product_addstock, name='product_addstock'),
]
