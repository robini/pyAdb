# coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8') 

import requests
from bs4 import BeautifulSoup
import bs4
import re


def getHtmlText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = "utf-8"
		#print r.encoding
		return r.text
	except:
		return ""

def parsePage(ilt,html):
	try:		
		soup = BeautifulSoup(html,"html.parser")
		#tag = soup.find_all('div',attrs={'class':'item'})
		tag = soup.find_all('li',attrs={'class':'intro'})
		for child in tag:
			if isinstance(child, bs4.element.Tag):
				#ilt.append(child.a['title'])
				ilt.append(child.string)
	except:
		print "wrong"

def printList(infolist,f):
	dic = {}	
#	count = 0			count = count+1
	for il in infolist:
		tags = il.split('/ ')
		for i in range(1,len(tags)):
			#print tags[i]
			if re.match('www',tags[i]):
				#print "none:"+str(i)
				break;
			if dic.has_key(tags[i])==True:
				dic[tags[i]] = dic[tags[i]] +1
			else:
				dic[tags[i]] = 1

	#zdic = zip(dic.values(),dic.keys())
#	dic = sorted(dic.values(),reverse = True)
	dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)
	#dkeys = dic.keys()
	for d in dic:
#		f.write(str(d)+"\n")
		f.write(str(d[0])+","+str(d[1])+"\n")

'''
		print count,g
		sys.setdefaultencoding(global_coding) 
		print count,global_coding
		f.write(str(count)+","+g+"\n")
		
		if count == 1:
			stt = g.split('/')
			print len(stt),stt[0],stt[3]
		f.write("")
'''

def main():
	
	url = 'https://www.douban.com/group/topic/112119066/'
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = "utf-8"
		#print r.encoding
		html =  r.text
	except:
		print "wrong"

	try:		
		soup = BeautifulSoup(html,"html.parser")
		#tag = soup.find_all('div',attrs={'class':'item'})
		tag = soup.find_all('div',attrs={'class':'reply-doc content'})
		for child in tag:
			if isinstance(child, bs4.element.Tag):
				#ilt.append(child.a['title'])
				#ilt.append(child.string)
				print child.p
	except:
		print "wrong"
main()

	


	










