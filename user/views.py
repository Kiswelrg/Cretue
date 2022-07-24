# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Record,Stuxh
from .models import Count
import datetime
from django.views.decorators.csrf import csrf_exempt
from user import isvalid,pyexc,jw2,jw,get
from user import extract as et
import json
from bs4 import BeautifulSoup
from django.utils import timezone
import pytz

# Create your views here.
# 
def count(request):
    count = Count.objects.get(id = 1)
    count.num += 1
    count.save()
    return HttpResponse('ok')

@csrf_exempt
def ret(request):
    if request.get_full_path()=="/ems/ret?mes=1" and not request.session.has_key('username'):
        return HttpResponseRedirect('/ems/ret')
    elif request.session.has_key('username') and request.session.has_key('ss') and request.get_full_path()!="/ems/ret?mes=1":
        return HttpResponseRedirect('/ems/ret?mes=1')
    else:
        return render(request,'ret.html')

def Index(request):
    # print(request.build_absolute_uri())
    if request.get_full_path()=="/?mes=1" and not request.session.has_key('username'):
        return HttpResponseRedirect('/')
    elif request.session.has_key('username') and request.session.has_key('ss') and request.get_full_path()!="/?mes=1":
        return HttpResponseRedirect('/?mes=1')
    else:
        return render(request,'index.html')

@csrf_exempt
def signin(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        return HttpResponseRedirect('/')
    else:
        mes = ""
        if request.GET.get("mes"):
            mes = request.GET.get('mes')
        return render(request, 'log.html', {'mes': mes})

@csrf_exempt
def getVCode(request):
    if request.method == "GET":
        if request.session.has_key('username') and request.session.has_key('ss'):
            return HttpResponseRedirect('/')
        else:
            sessionid = get.getJid(1)
            request.session['ss'] = sessionid
            vcode_image = isvalid.getCode(sessionid)
            return HttpResponse(vcode_image.getvalue(),'image/png')
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def login(request):
    if request.method == "POST":
        mode = request.POST.get('mode')
        if mode=='0' and request.POST.get('username') != '' and request.POST.get('password') != '':
            username = request.POST.get('username')
            password = request.POST.get('password')
            result = []
            if request.session.has_key('ss'):
                result = isvalid.isvalid0(username, password, request.session['ss'], request.POST.get('nick'))
            else:
                result = isvalid.isvalid0(username, password, '', '')
            print(result)
            if result[0] == True:
                request.session['username'] = username
                request.session['ss'] = result[1]
                print(username)
                print(result[1])
                #save record after valid user&password!
                if Record.objects.filter(id = username).exists() == True:
                    oldRec = Record.objects.get(id = username)
                else:
                    oldRec = Record()
                    oldRec.id = username

                if oldRec.keymode is None:
                    oldRec.keymode = 1
                else:
                    oldRec.keymode += 1
                oldRec.dateCreated =  timezone.now()
                oldRec.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('signin?mes=账号或密码有误!')
        elif mode == '1' and request.POST.get('ssid') != '':
            result = jw.getUserinfo(request.POST.get('ssid'))
            if result[2] is False:
                return HttpResponseRedirect('signin?mes=jssesionid无效!')
            else:
                print(request.POST.get('ssid'))
                print(result)
                request.session['username'] = result[0]
                request.session['ss'] = request.POST.get('ssid')
                username = request.session['username']
                if Record.objects.filter(id=username).exists():
                    oldRec = Record.objects.get(id=username)
                else:
                    oldRec = Record()
                    oldRec.id = username
                if oldRec.ssmode is None:
                    oldRec.ssmode = 1
                else:
                    oldRec.ssmode += 1
                oldRec.dateCreated = timezone.now()
                oldRec.save()
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('signin?mes=账号或密码错误!')
    else:
        return HttpResponseRedirect('signin?mes=账号或密码错误!')


def loginout(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        s = request.session['ss']
        del request.session['username'], request.session['ss']
        a = isvalid.isout(s)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('u\'r not even in')

@csrf_exempt
def transc(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        username = request.session['username']
        if Record.objects.filter(id = username).exists() == True:
            oldRec = Record.objects.get(id = username)
        else:
            oldRec = Record()
            oldRec.id = username
        #keep record when user is in !(no matter if userCode is valid)

        if len( request.POST.get('userCode')) == 11 or username == '16020031085':
            if oldRec.transc is None:
                oldRec.transc = 1
            else:
                oldRec.transc += 1
            oldRec.dateCreated = timezone.now()
            oldRec.save()

            if request.session['username'] == '16020031085':
                if request.POST.get('userCode') == '':
                    userCode = '16020031085'
                else:
                    userCode = request.POST.get('userCode')
            else:
                userCode = request.session['username']
            print(request.session['username']+' -> '+userCode)
            table = BeautifulSoup(jw2.getPoint(request.POST.get("nq"), request.POST.get("sjxz"), userCode, request.session['ss']), "html.parser")
            try:
                grade = table.find_all('table')[1]
            except IndexError:
                grade = 'no such number!'
            return HttpResponse(grade)
        else:
            if oldRec.error is None:
                oldRec.error = 1
            else:
                oldRec.error += 1
            #timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            oldRec.dateCreated = timezone.now()
            oldRec.save()
            return HttpResponse('/')
    else:
        return HttpResponse('plz login!')

@csrf_exempt
def coins(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        username = request.session['username']
        if Record.objects.filter(id = username).exists():
            oldRec = Record.objects.get(id = username)
        else:
            oldRec = Record()
            oldRec.id = username

        if len(request.POST.get('userCode')) == 8:
            if oldRec.lesson is None:
                oldRec.lesson = 1
            else:
                oldRec.lesson += 1
            oldRec.dateCreated = timezone.now()
            oldRec.save()
            #save record
            s = request.session['ss']
            
            # set current semester
            currentSemester = '2019-0'

            s1 = jw.listStudents(request.POST.get('userCode'), s, currentSemester)
            # try:
            lis = et.getCoin(et.getList(s1), request.POST.get('userCode'), s, currentSemester)
            # except:
            #     loginout(request)
            #     return HttpResponse("plz login!")
            if len(lis) > 0:
                return HttpResponse(json.dumps(lis,ensure_ascii=False))
            else:
                return HttpResponse('no such course!')
        else:
            if oldRec.error is None:
                oldRec.error = 1
            else:
                oldRec.error += 1
            oldRec.dateCreated = timezone.now()
            oldRec.save()
            return HttpResponse('no such course!')
    else:
        return HttpResponse('plz login!')


@csrf_exempt
def getGrades(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        username = request.session['username']
        if Record.objects.filter(id=username).exists():
            oldRec = Record.objects.get(id=username)
        else:
            oldRec = Record()
            oldRec.id = username
        print(request.POST.get('userCode'))
        if len(request.POST.get('userCode')) == 8:
            if oldRec.grades is None:
                oldRec.grades = 1
            else:
                oldRec.grades += 1
            oldRec.dateCreated = timezone.now()
            oldRec.save()
            #save record
            s = request.session['ss']
            xnxq = request.POST.get('nq')
            s1 = jw.listStudents(request.POST.get('userCode'), s, xnxq)
            lis = et.getScore(et.getList(s1), request.POST.get('userCode'), s, xnxq)
            # try:
            #     lis = et.getScore(et.getList(s1), request.POST.get('userCode'), s)
            # except:
            #     loginout(request)
            #     return HttpResponse("plz login!")
            if len(lis) > 0:
                print(lis)
                return HttpResponse(json.dumps(lis, ensure_ascii=False))
            else:
                return HttpResponse('no such course!')
        else:
            if oldRec.error is None:
                oldRec.error = 1
            else:
                oldRec.error += 1
            oldRec.dateCreated = timezone.now()
            oldRec.save()
            return HttpResponse('no such course!')
    else:
        return HttpResponse('plz login!')


@csrf_exempt
def alstd(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        username = request.session['username']
        if Record.objects.filter(id=username).exists():
            oldRec = Record.objects.get(id=username)
        else:
            oldRec = Record()
            oldRec.id = username
        if oldRec.selected is None:
            oldRec.selected = 1
        else:
            oldRec.selected += 1
        oldRec.dateCreated = timezone.now()
        oldRec.save()
        s = request.session['ss']
        if username == '16020031085':
            s1 = jw2.getSingle(request.POST.get('userCode')[:-6], s, request.POST.get('userCode')[-6:])
        else:
            s1 = jw2.getSingle(username, s, '2019-0')
        lis = et.inspect(s1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14])
        print(lis)
        return HttpResponse(json.dumps(lis, ensure_ascii=False))

    else:
        return HttpResponse('plz login!')


@csrf_exempt
def frd(request):
    if request.method == "POST":
        if request.session.has_key('username') and request.session.has_key('ss'):
            if request.POST.get("sel") == "0":
                print(request.POST.get('userCode'))
                try:
                    oldRec = Stuxh.objects.get(id=request.POST.get('userCode'))
                    return HttpResponse('[{"0":"' + request.POST.get('userCode')+'","1":"' + oldRec.name + '"}]')
                except:
                    return HttpResponse("no such person1!")
            else:
                try:
                    print(request.POST.get('userCode'))
                    oldRec = Stuxh.objects.filter(name=request.POST.get('userCode'))
                    if len(oldRec) < 1:
                        return HttpResponse("no such person!")
                    result = '['
                    for i in range(0,len(oldRec)):
                        print(oldRec[i].id)
                        result += '{"0":"' + oldRec[i].id + '","1":"' + request.POST.get('userCode') + '"},'
                    return HttpResponse(result[:-1] + ']')
                except:
                    return HttpResponse("no such person!")
        else:
            return HttpResponse('plz login!')
    else:
        return HttpResponseRedirect('/ret')

def getSS(request):
    if request.session.has_key('username') and request.session.has_key('ss'):
        return HttpResponse(request.session['ss'])
    else:
        return HttpResponse('plz login!')
