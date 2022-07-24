# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:33:41 2018

@author: ooo
"""

import requests
import random
import os

from bs4 import BeautifulSoup
os.environ['NO_PROXY'] = 'jwgl.ouc.edu.cn'
os.environ['NO_PROXY'] = 'ouc.edu.cn'


def listStudents(sel, si, xnxq):
    if si=='':
        si = 'D11E1B922E737H6F3AD2E875AA13C66J.kingo'
    a = random.randint(10,99)
    id = '160200310' + str(a)
    url = 'http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=3241&type=skbjdm'
    params = {'userId': id,
              'nj': xnxq[:4],
              'nj2': xnxq[:4],
              'emptyFlag': '0',
              'style': 'SKBJDM',
              'gradeController': 'on',
              'sel_role': 'ADM000',
              'xnxq': xnxq,
              'sel_skbjdm': sel,
              }
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
              6.99 Safari/537.36',
              'Referer': 'http://jwgl.ouc.edu.cn/common/popmsg/popmsg.sendOnlineMessage.jsp',
              'Cookie': 'JSESSIONID='+si,
              }
    s = requests.Session()
    r = s.post(url,data=params,headers=header)
    print('---'+si)
    return r.text


def getUserinfo(ss):
    url = 'http://jwgl.ouc.edu.cn/frame/desk/showSystemInfo.action'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
               6.99 Safari/537.36',
              'Referer': 'http://jwgl.ouc.edu.cn/MainFrm.html',
              'Cookie':'JSESSIONID=' + ss,
             }
    s = requests.Session()
    r = s.get(url, headers=header)
    info = ''
    userinfo = ['', '', True]
    if r.text[190] == "异":
        info = 'error'
        userinfo[2] = False
    else:
        soup = BeautifulSoup(r.text, "html.parser")
        info = str(soup.find('a', id='myinfo').string)
        userinfo = [info[1:12], info[13:], True]
    return userinfo

def getFaculty(ss):
    url = 'http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=2507'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339\
               6.99 Safari/537.36',
              'Referer': 'http://jwgl.ouc.edu.cn/student/stu.xsxj.zcxx.html?menucode=JW130202',
              'Cookie':'JSESSIONID=' + ss,
             }
    params = {
        'xh' : '16020031075',
    }
    s = requests.Session()
    r = s.post(url, data=params, headers=header)
    return r.text

#extract.getTableRow(getFaculty('A1E9003D082D63D995451B363EF7D1BA.kingo'),[-1],1)