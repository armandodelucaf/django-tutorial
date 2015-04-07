# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from dcc_colab import views as dcc_colab_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('dcc_colab.urls')),
    url(r'^home/$', dcc_colab_views.home, name='home'),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
