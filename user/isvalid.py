# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import requests as req
import base64
import hashlib
import time,urllib.parse
from PIL import Image
from user import get
from io import BytesIO

import time

os.environ['NO_PROXY'] = 'jwgl.ouc.edu.cn'


def getCode(ss):
    s = req.Session()
    s.trust_env = False
    tim = time.strftime('%c',time.localtime(time.time()))[:-13] + time.strftime('%Y %X',time.localtime(time.time())) + ' GMT+0800 (中国标准时间)'
    tim = urllib.parse.quote(tim)
    randnumber = ''
    header = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7,la;q=0.6',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
              6.99 Safari/537.36',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Referer': 'http://jwgl.ouc.edu.cn/cas/login.action',
              'Origin': 'http://jwgl.ouc.edu.cn',
              'Connection': 'keep-alive',
              'Host': 'jwgl.ouc.edu.cn',
              'Cookie': 'JSESSIONID='+ss,
              }
    url = 'http://jwgl.ouc.edu.cn/cas/genValidateCode?dateTime=' + tim
    r = s.get(url,headers=header)
    # buf = BytesIO(r.content)
    # return HttpResponse(buf.getvalue(), 'image/png')
    image = Image.open(BytesIO(r.content))
    #image.show()
    return BytesIO(r.content)

def isvalid0(xh, mm, ss, rand):
    mode0 = [True,'']
    #mode0 = ['0']*2
    s = req.Session()
    s.trust_env = False
    randnumber = ''
    if ss == '':
        sessionid = get.getJid(1)
    else:
        sessionid = ss
    randnumber = rand
    header = {'Accept': 'text/plain, */*; q=0.01',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
              6.99 Safari/537.36',
              'X-Requested-With': 'XMLHttpRequest',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Referer': 'http://jwgl.ouc.edu.cn/cas/login.action',
              'Origin': 'http://jwgl.ouc.edu.cn',
              'Connection': 'keep-alive',
              'Host': 'jwgl.ouc.edu.cn',
              'Cookie': 'JSESSIONID='+sessionid,
              }
    
    url = 'http://jwgl.ouc.edu.cn/cas/logon.action'
    username = xh
    password = mm
    policy = '1'
    p_username = '_u' + randnumber
    p_password = '_p' + randnumber
    rn = randnumber
    username = username + ';;' + sessionid
    username = base64.b64encode(username.encode('utf-8'))
    username = str(username,'utf-8')
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    randnumber = hashlib.md5(randnumber.encode('utf-8')).hexdigest()
    mix = hashlib.md5((password + randnumber).encode('utf-8')).hexdigest()
    
    params = p_username + "=" + username +\
        "&" + p_password + "=" + mix +\
        "&randnumber=" + rn +\
        "&isPasswordPolicy=" + policy
    s.trust_env = False
    r = s.post(url,data=params,headers=header)
    if r.text[12:13] == '操':
        mode0[0] = True
    elif r.text[12:13] == '帐':
        mode0[0] = False
    else:
        mode0[0] = False
        return 'fatal error (during login'
    print('- ' + str(mode0[0]) + ' -')
    mode0[1] = sessionid
    return mode0


def isvalid1(ss):
    start_time = time.time()
    s = req.Session()
    s.trust_env = False
    url = 'http://jwgl.ouc.edu.cn'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
               6.99 Safari/537.36',
              'Host': 'jwgl.ouc.edu.cn',
              'cookie': 'JSESSIONID='+ss,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    r = s.get(url,headers = header)
    print("--- %s seconds for 1 ! ---" % (time.time() - start_time))
    if r.text[7] == '\n':
        return True
    else:
        return False


def isvalid2(ss):
    start_time = time.time()
    s = req.Session()
    s.trust_env = False
    url = 'http://jwgl.ouc.edu.cn/frame/desk/showSystemInfo.action'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
               6.99 Safari/537.36',
              'cookie': 'JSESSIONID='+ss,
    }
    r = s.get(url,headers= header)
    print("--- %s seconds for 2 ! ---" % (time.time() - start_time))
    if r.text[-20:-19] == '>':
        return True
    else:
        return False


def isout(ss):
    s = req.Session()
    s.trust_env = False
    url = 'http://jwgl.ouc.edu.cn/DoLogoutServlet'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
    6.99 Safari/537.36',
              'Host': 'jwgl.ouc.edu.cn',
              'cookie': 'JSESSIONID='+ss,
              'Referer': 'http://jwgl.ouc.edu.cn/frame/Main_tools.jsp',
            }
    r = s.get(url,headers =header)
    if r.text != '!':
        return 'exit !'
    else:
        return 'exit err !'






