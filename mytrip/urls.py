# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

from mytrip import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^trips/$',views.trips,name='trips'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^register/$',views.regist,name='regist'),
	url(r'^home/$', views.home,name='home'),
	url(r'^trip/(?P<trip_id>\d+)/$',views.tripv,name='tripv'),
	url(r'^editfile/$',views.editfile,name='editfile'),
	url(r'^select/$',views.select,name='select'),
	url(r'^menu/$',views.menu,name='menu'),
	url(r'^intro/$',views.intro,name='intro'),
	url(r'^explore/$',views.explore,name='explore'),
	url(r'^collect/$',views.collect,name='collect'),
	url(r'^seetrip/(?P<trip_id>\d+)/$',views.seetrip,name='seetrip'),
	url(r'^search/(?P<choose>\w+)/$',views.search,name='search'),
	#url(r'^select/$',views.select,name='select'),
)
