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
	
	f = open("./testt","w")
	url_start = 'https://movie.douban.com/people/id?/collect?start='
	url_end = '&sort=time&rating=all&filter=all&mode=grid'
	depth = 1
	infolist = []
	for i in range(depth):
		try:
			url = url_start+str(15*i)+url_end
			html = getHtmlText(url)
			parsePage(infolist,html)
		except:
			continue
	printList(infolist,f)
	f.close()
#

main()

	


	















'''
r =  requests.get("https://movie.douban.com/people/chioich/collect?start=1&sort=time&rating=all&filter=all&mode=grid")
print type(r.status_code)
f = open("./testt","w")f.close()
f.write(r.text)	demo = "<p name='op' id='oid' class='oc'>ipppppppp ppio</p>"
https://movie.douban.com/people/chioich/collect
http://j.orz.asia/forum/T.asp?bID=3&replyid=6516479&id=263518&Star=5
for child in tag:
	if isinstance(child, bs4.element.Tag):
		print child.div.string


for child in tag:
	if isinstance(child, bs4.element.Tag):
		print child.a['title']
		#f.write(child.a['title'])

for cd in tag:
	if type(cd)==bs4.element.NavigableString :
		print cd
'''

#print tag.contents len(tag),type(tag[1])

#print type(tag.contents[0]),len(tag.contents[0])
#print type(tag.contents[1]),len(tag.contents[1])
#print soup.find_all('a')[0]
#print type(soup.find_all('a'))



'''
mm = soup.find_all('div','grid-view')
for child in soup.find('div','grid-view').children:
	print "----------------"
	print child
#print mm[4].contents
'''


#if r.status_code=='200'	print "succes"

#r.encoding='utf-8' print r.text

