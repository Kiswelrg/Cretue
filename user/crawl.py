
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Record,Stuxh
from user import jw,jw2,play
from user import extract as et
from django.views.decorators.csrf import csrf_exempt
from user import pyexc
# import datetime

# from bs4 import BeautifulSoup

# import base64,hashlib

@csrf_exempt
def collectStuxh(request):
	if request.POST.get('stud') != '' and request.POST.get('stunm') != '':
		a = Stuxh()
		a.id = request.POST.get('stuid')
		a.name = request.POST.get('stunm')
		a.save()
		return HttpResponse('ok')
	else:
		a = Stuxh()
		a.id = '16020031080'
		a.name = '五卅个'
		print('a.id')
		print('a.name')
		a.save()
		return HttpResponse('en!')

@csrf_exempt
def ctrl(request):
	return render(request, 'ctrl.html')

@csrf_exempt
def lic(request):
	if request.POST.get('stuid') != '':
		rt = jw.listStudents(request.POST.get('stuid'),request.session['ss'])
		return HttpResponse(et.fetchTable(rt, 1))
	else:
		return HttpResponse('error-')

@csrf_exempt
def sgl(request):
	if request.POST.get('stuid') != '':
		rt = jw2.getSingle(request.POST.get('stuid'),request.session['ss'])
		return HttpResponse(et.fetchTable(rt, 1))
	else:
		return HttpResponse('error-')

@csrf_exempt
def gameon(request):
	#play.playTheGame(request.POST.get('stuid'));
	print(pyexc.desenc('aaaaa','c'))
	print(pyexc.desenc('aa','c'))
	print(pyexc.desenc('a','c'))
	return HttpResponse('ßro, wowowowoowowowowowowowo!')
