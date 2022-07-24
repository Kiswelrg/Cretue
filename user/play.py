from user import extract,jw,jw2
import json
from bs4 import BeautifulSoup
from .models import Stuxh,offList6
from random import randint
from collections import deque
ss = '6B69B17B8656528FCD645C795BFE371F.kingo'
lessons = []

def getList13(text):
	soup = BeautifulSoup(text, "html.parser")
	i=0
	#ctnt = soup.tbody.contents[0:-1]
	ctnt = '['
	print(str(len(soup.tbody.contents)) + '--> tbody length')
	if len(soup.tbody.contents) != 0:
		for tr in soup.tbody.contents[0:-1]:
			a='{'
			for j in range(1,3):
				a = a + '"'+ str(j) +'":' + '"'+str(tr.contents[j].string) + '",'
			a = a[0:a.rindex(',')] + '},'
			ctnt += a
			i = i+1
	else:
		ctnt = '[{"1":"16020031075","2":"王刚"},'
	ctnt = ctnt[0:ctnt.rindex(',')]+']'
	return ctnt

def getList6(text):
	soup = BeautifulSoup(text, "html.parser")
	#ctnt = soup.tbody.contents[0:-1]
	print("=====" + str(len(soup.tbody.contents)))
	if len(soup.tbody.contents) > 2:
		j = randint(0,len(soup.tbody.contents)-2)
		a = str(soup.tbody.contents[j].contents[6].string)
		return a

def getList666(text):
	soup = BeautifulSoup(text, "html.parser")
	l = ['']
	print("=====" + str(len(soup.tbody.contents)))
	if len(soup.tbody.contents) > 2:
		for i in range(0,len(soup.tbody.contents)-2):
			l.append(str(soup.tbody.contents[i].contents[6].string))
	return l

def addRed(dic):
	#dic = json.loads(dict)
	for person in dic:
		p = Stuxh()
		p.id = person['1']
		p.name = person['2']
		p.save()

#print(p.id + ',' + p.name)

def playTheGame(sel):
	if offList6.objects.filter(lessonid = sel).exists() == False:
		print(sel)
		text = jw.listStudents(sel,ss)
		stus = json.loads(getList13(text))
		addRed(stus)
		crse = offList6()
		crse.lessonid = sel
		crse.save()
		#recuisive
		for person in stus:
			coursetxt = jw2.getSingle(person["1"],ss)
			randCourse = getList666(coursetxt)
			for sk in randCourse:
				playTheGame(sk)
			#playTheGame(randCourse)
