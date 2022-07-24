# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:33:41 2018

@author: ooo
"""

import requests
from user import pyexc
import base64
import hashlib
#import json
import time as TM
import os
os.environ['NO_PROXY'] = 'jwgl.ouc.edu.cn'
os.environ['NO_PROXY'] = 'ouc.edu.cn'


def getSingle(xh, si, xnxq):
    xh = xh
    url = 'http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=6093'
    params = {'electiveCourseForm.xktype': '2',
              'xn': xnxq[:4],
              'xq_m': xnxq[-1:],
              'xq': xnxq[-1:],
              'xh': xh,
              'text_weight': '0',
              'ck_gmjc': 'on',
              'ck_skbtj': 'on'}
    header = {'Referer': 'http://jwgl.ouc.edu.cn/student/wsxk.axkhksxk.html?menucode=JW130410',
              'Cookie': 'JSESSIONID=' + si}
    s = requests.Session()
    s.trust_env = False  
    r = s.post(url, data=params, headers=header)
    return r.text


def getKencrpt(ss):
    url = 'http://jwgl.ouc.edu.cn/custom/js/SetKingoEncypt.jsp'
    header = {
        'Cookie': 'JSESSIONID='+ss,
        'Host': 'jwgl.ouc.edu.cn',
        'Referer': 'http://jwgl.ouc.edu.cn/student/xscj.stuckcj.jsp?menucode=JW130705',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396\
        .99 Safari/537.36',
    }
    s = requests.Session()
    s.trust_env = False
    r = s.post(url, headers=header)
    a = ['']*2
    a[0] = r.text[19:38]
    a[1] = r.text[58:77]
    return a


def getPoint(xnxq, sjxz, xh, ss):
    tak = getKencrpt(ss)
    key = tak[0]
    time = tak[1]
    xn = xnxq[:4]
    xq = xnxq[-1:]
    xx = '&xnxq' + xnxq
    if sjxz == 'sjxz3':
        xx = ''
    param = 'xn=' + xn + '&xn1=2018' + '&xq=' + xq + '&ysyx=yscj' + '&sjxz=' + sjxz + '&userCode=' + xh + xx + '&ysyxS=on&sjxzS=on'
    print(param)
    print(key)
    start_time = TM.time()
    middle = pyexc.desenc(param, key)
    print("--- %s seconds ---" % (TM.time() - start_time))
    print(middle)
    params = base64.b64encode(middle.encode('utf-8')).decode('utf-8')
    # token part
    param = hashlib.md5(param.encode('utf-8')).hexdigest()
    tim = hashlib.md5(time.encode('utf-8')).hexdigest()
    token = hashlib.md5((param + tim).encode('utf-8')).hexdigest()
    params = 'params=' + params + '&token=' + token + '&timestamp=' + time
    #print(params)
    url = 'http://jwgl.ouc.edu.cn/student/xscj.stuckcj_data.jsp?' + params
    header = {
        'Cookie': 'JSESSIONID='+ss,
        'Host': 'jwgl.ouc.edu.cn',
        'Referer': 'http://jwgl.ouc.edu.cn/student/xscj.stuckcj.jsp?menucode=JW130705',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396\
        .99 Safari/537.36',
    }
    s = requests.Session()
    s.trust_env = False
    r = s.post(url, headers=header)
    return r.text


def coursename(xkh, ss, xnxq):
    url = 'http://jwgl.ouc.edu.cn/jw/common/getCourseInfoByXkh.action'
    params = {'xkh': xkh,
              'xn': xnxq[:4],
              'xq': xnxq[-1:],
              'xh': '16020031085',
              'hidOption': 'qry'
    }
    header = {
        'Cookie': 'JSESSIONID=' + ss,
    }
    s = requests.Session()
    s.trust_env = False
    r = s.post(url, data=params, headers=header)
    return r.text

def getArchive(si):
    url = 'http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=2507'
    params = {}
    header = {'Referer': 'http://jwgl.ouc.edu.cn/student/wsxk.axkhksxk.html?menucode=JW130202',
              'Cookie': 'JSESSIONID=' + si}
    s = requests.Session()
    s.trust_env = False  
    r = s.post(url, headers=header)
    return r.text
