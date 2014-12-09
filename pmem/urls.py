# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':  settings.STATIC_PATH}), 
	(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':  settings.MEDIA_PATH}),
	url(r'',include('social_auth.urls')),
	url(r'^facebook/', include('django_facebook.urls')),
	#url(r'^accounts/', include('django_facebook.auth_urls')), 
	#Don't add this line if you use django registration or userena for registration and auth
    url(r'^mytrip/', include('mytrip.urls')),	
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^$', 'pmem.mytrip.views.index'),	
)
