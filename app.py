import requests,random
from flask import Flask, jsonify, request



def rand(cho):
	login = [
	'https://instamoda.org/', 'https://takipcikrali.com/', 'https://takipstar.com/',
	'https://takipcigir.com/', 'https://takipcibase.com/', 'https://takipcimx.com/',
	'https://takipcizen.com/', 'https://takipciking.net/',
	'https://bayitakipci.com/member', 'https://begenivar.com/']
	mem = [
	'https://hepsitakipci.com/', 'https://fastfollow.in/']
	if cho == "login":
		hhh = random.choice(login)+str('login')
	elif cho == "mem":
		hhh = random.choice(mem)+str('member')
	return hhh


app = Flask(__name__)

@app.route('/login/username=<username>/password=<password>/by/cc_02', methods=['GET'])
def login(username,password):
	url = rand(random.choice(['login','mem']))
	
	payload = {
		'username':f'{username}',
		'password':f'{password}'
	}
	
	
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
	
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	if '"status":"success"' in response.text:
		return jsonify({
			'status':True,
			'message':'Done Login',
			'username':str(username),
			'password':str(password),
			'by':'cc_02'
		})
	else:
		return jsonify({
			'status':False,
			'message':'bad Login',
			'username':str(username),
			'password':str(password),
			'by':'cc_02'
		})



if __name__ == '__main__':
    app.run(debug=True)
