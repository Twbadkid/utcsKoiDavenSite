# -*- coding:utf-8 -*-
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
import datetime
from django.utils.translation import ugettext as _
from django.template import Template,RequestContext,Context
from mytrip.models import Trip,User,Trip_Location,Trip_Perform,Collect
from django.core.context_processors import csrf 
#from django.views.decorators.csrf import csrf_protect
# Create your views here.

class UserForm(forms.Form):
#	class Meta:
#		model = User
	user_id = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	#repassword = forms.CharField(widget = forms.PasswordInput)
	email = forms.EmailField(required = False )
	name = forms.CharField()

class LoginForm(forms.Form):
	user_id = forms.CharField(max_length=30)
	password = forms.CharField(widget = forms.PasswordInput)

class TempForm(forms.Form):
	public = forms.BooleanField(required=False,initial=True,)
	style = forms.ChoiceField(choices=[('style1','天空藍'),('style2','純白'),('style3','特別的蓋子')])

class SearchForm(forms.Form):
	name = forms.CharField(max_length=30)

class CollectForm(forms.Form):
	likes = forms.IntegerField(min_value=0)

def index(request):
	#return HttpResponseRedirect('/mytrip/home/')
	username = request.session.get('user_id')#'anybody'
	return render_to_response('mytrip/index_m.html',{'username': username})
	#now=datetime.datetime.now()
	#t=Template('<html><body>now is time:{{current_date}}</body></html>')
	#c=Context({'current_date':now})
	#html=t.render(c)
	#return HttpResponse(html)
	#return HttpResponse("Hi! this is my trip index.")

def intro(request):
	username = request.session.get('user_id')#'anybody'
        return render_to_response('mytrip/intro.html',{'username': username})

def explore(request):
	username = request.session.get('user_id')
	if username == None:
                return render_to_response('mytrip/explore.html',{})
        else:
                return render_to_response('mytrip/explore.html',{'username':username})

def collect(request):
	username = request.session.get('user_id')
	if username == None:
		return HttpResponseRedirect('/mytrip/')
	else:
		return render_to_response('mytrip/collect.html',{'username':username})

def seetrip(request, trip_id):
	idno=int(trip_id)
	username = request.session.get('user_id')
	#msg = User.objects.filter(user_id__exact= user_id)
	#userid = User.objects.get(user_id = username).idnum
	#userid = 
	if username == None:
		if Trip_Perform.objects.filter(tripid = idno):
                	tripid=Trip.objects.get(trip_id = idno).trip_id
        	else:
			msg="This trip is private!"
        	       	return HttpResponseRedirect('/mytrip/explore/')
		return render_to_response('mytrip/seetrip.html',{'idno':idno})	
	else:
		userid = User.objects.get(user_id = username).idnum
		tuid= Trip.objects.get(trip_id = idno).uid_id
		if str(userid) == str(tuid):
			owner= True
		else:
			owner=False
		if request.method == 'POST':
			if owner ==True:
				form= TempForm(request.POST)#save trip style&public
				check = request.REQUEST.get('public')
				if check == "on":
                	              	permi=True
                        	else:
                                	permi=False
                        	if form.is_valid():
                                	style = form.cleaned_data['style']
                                	if style =="style1":
                                        	style=1
                                	elif style=="style2":
                                        	style=2
					elif style =="style3":
						style=3
				strip=Trip(trip_id = idno)
                               	t=Trip_Perform()
                               	t.tripid=strip
                               	t.permission=permi
                               	t.data=style
                               	t.save()
			else:
				form = CollectForm()
				li=True
		#elif 'likes' in request.POST:
			#c=Collect()
			#c.user_id=username
			#c.tripid=idno
			#c.save()
			#l=Trip()
			#l.likes+=1
			#l.save()
		else:
			if owner!= True:
				form= CollectForm()
				#return render_to_response('mytrip/seetrip.html',{'tuid':tuid,'idno':idno,'username':username,'form':form,'userid':userid},context_instance=RequestContext(request))
			else:
				form = TempForm()
		return render_to_response('mytrip/seetrip.html',{'owner':owner,'tuid':tuid,'idno':idno,'username':username,'form':form,'userid':userid},context_instance=RequestContext(request))
##		#if Trip.objects.filter(trip_id = idno):
		#	if Trip.objects.filter(uid = username):#自己的紀錄->修改
		#		return  render_to_response('mytrip/seetrip.html',{'tripid':tripid}
		#	else:#看別人的紀錄->收藏+喜歡
		#		return render_to_response('mytrip/seetrip.html',{'username':username, 'trip_id':trip_id})
		#else:
		#	return HttpResponseRedirect('/mytrip/home/')
	
def login(req):  
    if req.method == 'POST':  
        uf = LoginForm(req.POST)  
        if uf.is_valid():  
            user_id = uf.cleaned_data['user_id']  
            password = uf.cleaned_data['password']  
            user = User.objects.filter(user_id__exact = user_id,password__exact = password)  
            if user:  
                req.session['user_id'] = user_id  
                return HttpResponseRedirect('/mytrip/')  
            else:  
                err = -1 
                #return HttpResponseRedirect('/mytrip/login')	
		return render_to_response('mytrip/login.html',{'err':err, 'uf':uf}, context_instance=RequestContext(req))
    else:  
        uf = UserForm()  
    return render_to_response('mytrip/login.html',{'uf':uf}, context_instance=RequestContext(req))

def menu(request):
	return render_to_response('mytrip/menu.html',{},)

def trips(request):
	#triptid = Trip_Location.objects.get(tid)
	user_id = request.session.get('user_id')
	if user_id == None:
		return HttpResponseRedirect('/mytrip/login/')
	else:
		if User.objects.filter(user_id__exact=user_id):
			uid = User.objects.get(user_id = user_id).idnum
			#tid += Trip.objects.get(uid_id = uid).trip_idi
			if Trip.objects.filter(uid_id__exact = uid):
				trips = Trip.objects.filter(uid_id__exact=uid)
				tripl = Trip_Location.objects.all()
				return render(request,'mytrip/trips.html',{'trips' : trips, 'tripl':tripl})
			else:
				msg = '來記錄屬於自己的第一個旅行吧'
				return render(request,'mytrip/trips.html',{ 'msg':msg})

def regist(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		err = 'invalid user account or password, please input again!'  
		if uf.is_valid():
			no = User.objects.count()
			if no == None:
				no = 1
			else:
				no = no+1
			user_id = uf.cleaned_data['user_id']
			password = uf.cleaned_data['password']
			#repassword = uf.cleaned_data['repassword']
			#if password != repassword:
				#return HttpResponse('password is not correct.')
			email = uf.cleaned_data['email']
			name = uf.cleaned_data['name']
			if User.objects.filter(user_id__exact=user_id):
				return render_to_response('mytrip/register.html',{'uf':uf,'err':err})
			User.objects.create(user_id = user_id, password = password,idnum = no,email = email, name = name)
			request.session['user_id'] = user_id
			return HttpResponseRedirect('/mytrip/login/')
	else:
		uf = UserForm()
	return render_to_response('mytrip/register.html',{'uf':uf},context_instance=RequestContext(request))

def logout(request):
	session = request.session.get('user_id')#, False
	if session:
		del request.session['user_id']
		return HttpResponseRedirect('/mytrip/')
		#return render_to_response('mytrip/logout.html',{'user_id':session})
	else:
		return HttpResponseRedirect('/mytrip/')

def home(request):
	user_id = request.session.get('user_id')
	if user_id == None:
		return HttpResponseRedirect('/mytrip/login/')
	else:
		#if request.method =='POST':
                #	temps= request.POST['choice']
                #	if temps.is_valid():
                #        	style = temps.cleaned_data['style']
		#else:
		#	temps=TempForm()
		msg = User.objects.filter(user_id__exact= user_id)
		user = User.objects.get(user_id = user_id).idnum
		triplist=Trip.objects.filter(uid_id__exact=user)
		return render_to_response('mytrip/userpage.html',{'msg':msg ,'user_id':user_id,'triplist':triplist,},context_instance=RequestContext(request))

def editfile(request):
	user_id = request.session.get('user_id')
	if request.method =='POST':
		msg = UserForm(request.POST)
		if msg.is_valid():
			name = msg.cleaned_data['name']
			password = msg.cleaned_data['password']
			repassword = msg.cleaned_data['password']
			email = msg.cleaned_data['email']
			if password != repassword:
                       		return HttpResponse('password is not correct.')
			
			#user=User.objects.get(user_id__exact=user_id)
			#f=UserForm(request.POST, instance=user)
			user = User.objects.get(user_id__exact=user_id)
			user.email=email
			user.name=name
			user.password=password
			user.save()
			#User.objects.filter(user_id__exact=user_id).update(name= name)
			#User.objects.filter(user_id__exact=user_id).update(password = password)
			#User.objects.filter(user_id__exact=user_id).update(email = email)
		return HttpResponseRedirect('/mytrip/editfile/')
		#profile = User.objects.filter(user_id__exact= user_id)
                #user = User.objects.get(user_id = user_id).idnum
	else:
		if user_id == None:
			#msg= UserForm()
			return HttpResponseRedirect('/mytrip/')
		else:
	 		profile = User.objects.filter(user_id__exact= user_id)
         		user = User.objects.get(user_id = user_id).idnum
		msg= UserForm()
        return render_to_response('mytrip/editfile.html',{'msg':msg, 'profile':profile , 'user_id':user_id},context_instance=RequestContext(request))	

def tripv(request, trip_id):
	idno=int(trip_id)
	user_id = request.session.get('user_id')
	if Trip_Location.objects.filter(tid__exact = idno):
		if Trip_Perform.objects.filter(tripid = idno):
			ifpublic=Trip_Perform.objects.get(tripid = idno).permission
			if ifpublic == True:
				temps=Trip_Perform.objects.get(tripid =idno).data
			else:
				temps=2	
		else:
			temps=1
		tripn=Trip.objects.get(trip_id = idno).trip_name
                tripv=Trip_Location.objects.filter(tid__exact= idno)
		if temps=="1":
			return render_to_response('mytrip/tripv.html',{'tripv':tripv,'tripn':tripn})
		elif temps=="3":
			return render_to_response('mytrip/tripv3.html',{'tripv':tripv,'tripn':tripn})
		else:
			return render_to_response('mytrip/tripv1.html',{'tripv':tripv, 'tripn':tripn,'temps':temps})
		#return render_to_response('mytrip/tripv1.html',{'tripn':tripn,'tripv':tripv, 'temps':temps})
	else:
		msg='No trip id for this trip!'	
		return render_to_response('mytrip/tripv1.html',{'msg':msg})


def select(request):
	user_id = request.session.get('user_id')
        if user_id == None:
                return HttpResponseRedirect('/mytrip/login/')
        else:
		if request.method =='POST':
                        temps= TempForm(request.POST)
			#ifpubl = request.REQUEST.getlist('ifpubl')
			check = request.REQUEST.get('check')
			if check == "1":
				permi="True"
				h=True
			else:
				permi="False"
				h=False	
                        if temps.is_valid():
                                style = temps.cleaned_data['style']
				if style =="style1":
					style=1
				else:
					style=2
			try:
				no=request.POST['whicht']
			except  KeyError: 
				msg='please select one trip!'
				temps=TempForm()
                		#if User.objects.filter(user_id__exact=user_id):
                        	uid = User.objects.get(user_id = user_id).idnum
                        	triplist=Trip.objects.filter(uid_id__exact=uid)
        			return render_to_response('mytrip/seetrip.html',{'user_id':user_id,'uid': uid , 'triplist':triplist ,'temps':temps,'msg':msg},context_instance=RequestContext(request))
			else:
				whichtrip=Trip.objects.get(trip_id = no).trip_name
				strip=Trip(trip_id = no)
				t=Trip_Perform()
				t.tripid=strip
				t.permission=h
				t.data=style
				t.save()
				msg='please select one trip!'	
			return HttpResponseRedirect('/mytrip/home/')
			#whichstyle=style
			#t=Template('<html><body>{{ no }}<p>which trip:{{ whichtrip }} </p><p>which style:{{ whichstyle }}</p><p> if public:{{ ifpubl }} {{ permi }}</p> <a href="/mytrip/home">Goback</a></body></html>')
        		#c=Context({'no':no,'whichtrip':whichtrip,'whichstyle':whichstyle,'ifpubl':ifpubl ,'permi':permi})
        		#html=t.render(c)
        		#return HttpResponse(html)
			#return render_to_response('mytrip/tripv.html',{'no':no,'h': h , 'whichtrip':whichtrip ,'style':style})			
                else:
                        temps=TempForm()
                if User.objects.filter(user_id__exact=user_id):
                        uid = User.objects.get(user_id = user_id).idnum
			triplist=Trip.objects.filter(uid_id__exact=uid)
	return render_to_response('mytrip/seetrip.html',{'user_id':user_id, 'uid': uid , 'triplist':triplist ,'temps':temps},context_instance=RequestContext(request))

def search(request, choose):
	if choose == "location":
		if request.method =='POST':
                	msg = SearchForm(request.POST)
                	if msg.is_valid():  
        			uname = msg.cleaned_data['name']
        			users = User.objects.filter(name__icontains = uname)
			else:
				users= "oh" 
		else:
			msg= SearchForm()
			users = "no"
		tlocate = Trip_Location.objects.all()
		#if Trip_perform.objects.filter(permission__exact=True):
		#	tlist = Trip_perform.objects.get(permission =True).tripid
		return render_to_response('mytrip/search.html',{'tlocate':tlocate,'users':users},context_instance=RequestContext(request))
	elif choose == "photo":
		tlocate = Trip_Location.objects.all()
		return render_to_response('mytrip/search.html',{'tlocate':tlocate})
	elif choose =="trips":
		tlocate = Trip_Perform.objects.all()
		return render_to_response('mytrip/search.html',{'tlocate':tlocate})
	else:
		return HttpResponseRedirect('/mytrip/')

		
