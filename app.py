import requests
from user_agent import *

def fragment(username):
	url = f"https://fragment.com/username/{username}"
	headers = {
		'User-Agent': generate_user_agent(),
		'Accept': "application/json, text/javascript, */*; q=0.01",
		'X-Requested-With': "XMLHttpRequest",
		'Sec-Fetch-Site': "same-origin",}
	r = requests.post(url,headers=headers).text
	print(r)
	if '?query' in r:
		return True
	elif 'Someone already claimed this username on Telegram.' in r:
		return 'is taken'
	else:
		return False
while True:
	print(fragment('u_l_kekew'))
