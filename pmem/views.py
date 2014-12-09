# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the first page.") 
