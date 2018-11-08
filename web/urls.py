from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index_redirect, name='index_redirect'),
    url(r'^crud/', include('crud.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
