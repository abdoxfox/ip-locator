import json
import requests
import time,sys
from colorama import Style,Back

def welcoming(str):
	for c in str + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)
welcoming('welcome to my script\nmy nickname abdoxfox & my telegram ID is @Pythonest\nthis program will show you all info about your ip')
welcoming('\nyour ip adrress and geolocal is :')
api='https://geoip-db.com/json/geoip.php?json'

response =requests.get(api)

jsinfo=response.text
dict = json.loads(jsinfo)
for i,v in dict.items():
	print(f'{Back.BLUE}{i} -----------> {v}\n ')
print(Style.RESET_ALL) 
welcoming('do you want to save info ?')
userinfo=input('[y/n] :')
if userinfo =='Y' or userinfo=='y':
	f=open('ipAdrress.txt','w')
	for i,v in dict.items():
		f.write(f'{i} -----> {v}\n')
	f.close()
elif userinfo=='N' or userinfo=='n':
	print('as you like');print('thanks using my script ')
else:
	print('choix invalid retry again ')
	
