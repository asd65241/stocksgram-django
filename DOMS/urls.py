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
from django.conf.urls import url, include
from django.contrib import admin
from dashboard import views as dashboard
from orders import views as order
from customers import views as customer
from products import views as product
from inventory import views as inventory
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard.index, name='dashboard'),
    url(r'^orders$', order.index, name='orders_home'),
    url(r'^order/', include('orders.urls')),
    url(r'^customers$', customer.index, name='customers_home'),
    url(r'^customer/', include('customers.urls')),
    url(r'^products$', product.index_product, name='products_home'),
    url(r'^product/', include('products.urls')),
    url(r'^inventories$', inventory.index, name='inventory_home'),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^fileupload/', include('fileupload.urls')),
    url(r'^users/login/$', auth.LoginView.as_view(),
        {'template_name': 'login.html'}, name='login'),
    url(r'^users/logout/$', auth.LogoutView.as_view(),
        {'next_page': '/'}, name='logout'),
    url(r'^users/change_password/$',
        login_required(auth.PasswordChangeView.as_view()), name='change_password'),
]

# url(r'^orders$', my_order.index, name='home'),
# url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
# url(r'^order/new/$', my_order.new, name='new'),
# url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
# url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
