#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import time

date=time.strftime('%Y-%m-%d', time.localtime())
Cdate=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

sqrid='209751'  #未知
sqbmid='350'   #未知

sqrmc='孙敏' #姓名
gh='192210711223'#学号
sqbmmc='计算机学院' #学院
sfzh='320826200101302613'#身份证号
jgshen='江苏省' #省份
jgshi='淮安市'#市
lxdh='13852332553'#手机号



tbrq=str(date)
tjsj=str(Cdate)
glqsrq="[\""+tbrq+"\",\""+tbrq+"\"]"



Fpayload ={"entity":{"sqrid":sqrid,"sqbmid":sqbmid,"rysf":"1","sqrmc":sqrmc,"gh":gh,"sqbmmc":sqbmmc,"sfzh":sfzh,"xb":"1","jgshen":jgshen,"jgshi":jgshi,"lxdh":lxdh,"tbrq":tbrq,"jrszd":"学校","jrstzk":"当日有发热咳嗽等疑似症状","sfjchwry":"否","sfyyqryjc":"否","sfyqgzdyqryjc":"否","sfjcysqzrq":"否","jrsfjgzgfxdq":"否","jgzgfxdq":"","sflz":"否","lzsj":"","lzjtgj":"","lzbc":"","sffz":"空","fhzjsj":"","fhzjgj":"","fhzjbc":"","fztztkdd":"","glqsrq": glqsrq,"sffr":"否","tw":"37","zwtw":"37","jrjzdxxdz":"江苏科技大学","bz":"","_ext":"{}","tjsj":tjsj}}

s=requests.session() 
headers = {
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Content-Type': 'application/x-www-form-urlencoded',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
}
execution=s.get('http://ids2.just.edu.cn/cas/login',headers=headers)

a=re.findall('"execution" value="(.*)"', execution.text)
#print(a[0])
cookies=execution.cookies
#print(cookies)
username='192210711223'
password='Sunmin666'

url = "http://ids2.just.edu.cn/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F"

payload='username='+username+'&password='+password+'&rememberUsername=off&rememberPassword=off&execution='+a[0]+'&_eventId=submit&loginType=1&submit=%25E7%2599%25BB%2B%25E5%25BD%2595'
headers = {
  'Referer': 'http://ids2.just.edu.cn/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F',
  'Accept-Encoding': 'gzip, deflate',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'SESSION='+cookies['SESSION']+';route='+cookies['route']
}

response = s.request("POST", url, headers=headers, data=payload)


cas=response.cookies
print(cas)
#print(response.headers)



#print(response.cookies)

url = "http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp"

headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie':  'SESSION='+cookies['SESSION']+'route='+cookies['route']+'CASTGC='+cas['CASTGC']+';'
}
response = s.get(url,headers=headers,allow_redirects=False)


#print(response.headers)
location=response.headers['Location']
print(location)
j=response.cookies
print(j)
url =location

headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie':  'SESSION='+cookies['SESSION']+';CASTGC='+cas['CASTGC']+';'+'route='+cookies['route']
}
response = s.get(url,headers=headers,allow_redirects=False)
#print(response.headers)
location=response.headers['Location']

url =location

headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie':  'JSESSIONID='+j['JSESSIONID']+';route='+j['route'],
}
response = s.get(url,headers=headers,allow_redirects=False)
#print(response.headers)
location=response.headers['Location']

url =location

headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie':  'JSESSIONID='+j['JSESSIONID']+';route='+j['route'],
}
response = s.get(url,headers=headers,allow_redirects=False)
#print(response.text)


url = "http://ehall.just.edu.cn/default/work/jkd/jkxxtb/com.sudytech.work.suda.jkxxtb.jktbSave.save.biz.ext"

headers = {
  'Connection': 'keep-alive',
  'Accept': '*/*',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
  'Content-Type': 'text/json',
  'Origin': 'http://ehall.just.edu.cn',
  'Referer': 'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Cookie':  'JSESSIONID='+j['JSESSIONID']+';route='+j['route'] ,
  'Referer':'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp'
}

response = requests.request("POST", url, headers=headers, data=str(Fpayload).encode('utf-8'),allow_redirects=False)

print(response.text)

