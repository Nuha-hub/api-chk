import requests,re,random,time
from flask import Flask, jsonify, request
from user_agent import *





app = Flask(__name__)

@app.route('/check/email=<email>/by/cc_02', methods=['GET'])
def chk(email):
	ma = requests.Session()
	passwor = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:hassan11inthetop878n"
	rs3 = ma.get('https://www.instagram.com/accounts/login/')
	ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
	headers = {
	            "user-agent": generate_user_agent(),
	            "x-csrftoken": ctk,
	            "x-ig-www-claim": "0",
	        }
	rs3 = ma.post(
	            "https://www.instagram.com/api/v1/web/accounts/login/ajax/",
	            headers=headers,
	data={
	                "enc_password": passwor,
	                "username": email,
	                "queryParams": "{}",
	                "optIntoOneTap": "false",
	                "trustedDeviceRecords": "{}"
	            },
	        )
	
	headers.update({"x-ig-set-www-claim":"0"})
	headers.update({"x-csrftoken": ctk})
	if 'html' in rs3.text:
		return jsonify({
			'by':'@cc_02',
			'email':f'{email}',
			'message':'Available iG',
			'status':True
		})
	else:
		return jsonify({
			'by':'@cc_02',
			'email':f'{email}',
			'message':'unAvailable iG',
			'status':False
		})



if __name__ == '__main__':
    app.run(debug=True)
