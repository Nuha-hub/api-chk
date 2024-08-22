from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def chk(user, password, user_agent):
	headers = {
		'user-agent': user_agent,
		'x-csrftoken': 'DR5b4AGM6JJEVVHNUvKWBk6uXoBIke47',
		'x-ig-www-claim': '0'
		}
	data = {
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
		'etoken': 'AbgL8JrGd3MCKSnptsaJ8K-FABbYtm0hiQ7h4-mvHvHcpgwP6daZ5fOU4bzGAXp9x_74Q8yQ6uIIR2BOWlfInvau7bruwonmn6W4ne8Y2xusSwwnHPT62U1m',
		'username': user
		}
	response = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', headers=headers, data=data)
	if '"authenticated":true' in response.text:return True
	elif 'checkpoint_required' in response.text:return 'secure'
	else:return False

@app.route('/login/usernmae=<username>/password=<password>/by/cc_02', methods=['GET'])
def login(username, password):
	user_agent = request.headers.get('User-Agent')
	
	return jsonify({'authenticated':chk(username,password,user_agent)})
	

if __name__ == '__main__':
	app.run(debug=False)
