# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:15:35 2018

@author: Administrator
"""

import requests

def getJid(op):
    s = requests.Session()
    if op==2:
        r = s.get('http://jwgl.ouc.edu.cn/custom/js/SetKingoEncypt.jsp')
    elif op==1:
        r = s.get('http://jwgl.ouc.edu.cn/cas/login.action',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                })
    a = ''
    a = r.headers['Set-Cookie']
    #print(r.headers)
    return a[11:a.rindex(';')]
