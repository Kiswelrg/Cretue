# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:07:27 2018

@author: ooo
"""
from user import jw,jw2
import json
import time
from bs4 import BeautifulSoup

def getList(text):
    start_time = time.time()
    #htmlPage = open(file)
    soup = BeautifulSoup(text, "html.parser")
    i=0
    ctnt = soup.tbody.contents[:-1]
    for tr in soup.tbody.contents[:-1]:
        a='{'
        for j in range(1,4):
            a = a + '"'+ str(j) +'":' + '"'+str(tr.contents[j].string) + '",'
        a = a[0:a.rindex(',')] + '}'
        ctnt[i] = a
        print(a)
        i = i+1
    print('fetch list complete!')
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(ctnt))
    return ctnt


def inspect(data, indexs):
    # htmlPage = open(data)
    # print(htmlPage)
    soup = BeautifulSoup(data, "html.parser")
    ctnt = []
    for tr in soup.tbody.contents[:-1]:
        a = '{'
        for j in indexs:            #0 1 2 6 8 13
            a = a + '"' + str(j) + '":' + '"'+str(tr.contents[j].string) + '",'
        a = a[0:a.rindex(',')] + '}'
        ctnt.append(json.loads(a))
    return ctnt


def getCoin(cntn, sel, si, xnxq):
    a = 0
    jso = []
    for xh in cntn[0:]:
        start_time = time.time()
        xx = json.loads(xh)
        cor = getCors(jw2.getSingle(xx["1"], si, xnxq), sel)
        xx["0"] = cor[0]
        xx["4"] = cor[2]
        xx['5'] = cor[1]
        jso.append(xx)
        print("--- %s seconds for 1 Cor ---" % (time.time() - start_time))
        a += (time.time() - start_time)
    jso.sort(key = lambda x: x["0"], reverse=True)
    print("--- %s seconds totally ---" % a)
    return jso


def getScore(cntn, sel, si, xnxq):
    start_time = time.time()
    a = 0
    jso = []
    #print(jw2.coursename(sel, si, xnxq))
    name = json.loads(jw2.coursename(sel, si, xnxq))[0]["kcmc"]
    print(name)
    for xh in cntn[0:]:
        start_time = time.time()
        xx = json.loads(xh)
        try:
            xx["0"] = getSors(jw2.getPoint(xnxq, 'sjxz3', xx["1"], si), name)
        except:
            xx["0"] = 'unknown'
        jso.append(xx)
        print("--- %s seconds for 1 Cor ---" % (time.time() - start_time))
        a += (time.time() - start_time)
    jso.sort(key=lambda x: x["0"], reverse=True)
    print("--- %s seconds totally ---" % a)
    return jso


def show(coin):
    i=0
    #length = len(coin)
    coin.sort(key = lambda x: x["0"], reverse=True)
    try:
        for xx in coin:
            i += 1
            print('%-4s' % str(i) + '%-4s' % str(xx["0"]) + '  ' + xx["1"]+'  '+xx["2"]+'  '+xx["3"]+'  '+xx["4"]+'  '+xx["5"])
    except:
        i = 0
        for xx in coin:
            i+=1
            print('%-4s' % str(i) + '%-4s' % str(xx["0"]) + '  ' + xx["1"]+'  '+xx["2"])


def getCors(stri, sel):
    soup = BeautifulSoup(stri, "html.parser")
    Cor = [0, 'un', True]
    for tr in soup.tbody.contents:
        if tr.contents[6].string == sel:
            coin = int(tr.contents[8].string)
            state = tr.contents[13].string
            Cor[0] = coin
            Cor[2] = state
            if len(str(tr.contents[11].input)) > 40:
                Cor[1] = True
            else:
                Cor[1] = False
            return Cor
    return Cor


def getSors(stri, name):
    soup = BeautifulSoup(stri, "html.parser")
    Cor = ''
    for tr in soup.tbody.findChildren('tr'):
        if name in str(tr.findChildren('td')[1].string):
            Cor = str(tr.findChildren('td')[6].string)
            return Cor
    return Cor


def fetchTable(txt, index):
    soup = BeautifulSoup(txt, "html.parser")
    return soup.findAll('table')[index-1]


def lastRow(t):
    soup = BeautifulSoup(t, "html.parser")
    tr = soup.find_all('tr')[-1].find_all('td')
    return [(str(tr[2].string)), (str(tr[3].string))]

def getTableRow(txt, nums, tableIndex):
    # default contains thead
    soup = BeautifulSoup(txt, "html.parser")
    tableTr = soup.findAll('table')[tableIndex-1].findAll('tr')
    result = ['']
    for i in nums:
        tds = tableTr[i].findAll('td')
        for td in tds:
            result.append(td.string)
    return result