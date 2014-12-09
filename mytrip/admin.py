# -*- coding:utf-8 -*-
from django.contrib import admin
from mytrip.models import User,Local,Trip,Trip_Location,Trip_Perform,Collect
#from mytrip.models import Local

class UserAdmin(admin.ModelAdmin):
	list_display = ('idnum', 'user_id')

class LocalAdmin(admin.ModelAdmin):
	list_display =('local_name', 'local_id')

class TripAdmin(admin.ModelAdmin):
	list_display= ('uid_id', 'trip_id', 'trip_name', 'trip_date')
	list_filter = ['trip_date'] #右边小窗过滤器

class TripLAdmin(admin.ModelAdmin):
	list_display= ('no','tid','lid', 'dtime')
	
class TripPAdmin(admin.ModelAdmin):
	list_display= ('tripid','modify_time','permission')

class CollectAdmin(admin.ModelAdmin):
	list_display= ('userid','ctrip')

admin.site.register(Trip_Location,TripLAdmin)
admin.site.register(Trip_Perform,TripPAdmin)
admin.site.register(Local,LocalAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Trip,TripAdmin)
admin.site.register(Collect,CollectAdmin)
#admin.site.register(UserAdmin)
