import requests,random,secrets
from user_agent import generate_user_agent
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/check/id=<re>/by/cc_02', methods=['GET'])
def search(re):
	try:
		csrftoken = secrets.token_hex(32)
		mid=secrets.token_hex(27)
		ig_=secrets.token_hex(36)
		datr=secrets.token_hex(24)
		app=''.join(random.choice('936619743392459')for i in range(15))
		cookies = {
			'csrftoken': csrftoken,
			'ps_l': '0',
			'ps_n': '0',
			'ig_did': f'{ig_}',
			'ig_nrcb': '1',
			'dpr': '2.1988937854766846',
			'mid': mid,
			'datr': datr,
}
		headers = {
			'sec-fetch-site': 'same-origin',
			'viewport-width': '891',
			'x-asbd-id': '129477',
			'user-agent':generate_user_agent(),
			'x-csrftoken': csrftoken,
			'x-ig-app-id': app,
			'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
			'x-fb-lsd': 'AVoRhvRPoRs',
}


		data = {
			'csr': 'gVb2snsIjkIQyjRmBaFGECih59Fb98nQBzbZ2IN8BqBGl7h9Am4ohAAD-vGBh4GizA-4aAiJ2vFDUR3qx596AhrBgzJlBKmu6VHiypryUkByrGiicgPAx6iUpGEOmqfykFA4801kXEkOwmU1Tqwvk8wCix64E0b_EaWdguwozat2F61-wiokxG0d9w2MFU5Kzo0k6wiU7Kut2F601_Ew1me',
			'lsd': 'AVoRhvRPoRs',
			'variables': '{"id":"'+re+'"}',
			'server_timestamps': 'true',
			'doc_id': '7381344031985950',
}

		response = requests.post('https://www.instagram.com/api/graphql',cookies=cookies,  headers=headers, data=data).json()
		full_name = response['data']['user']['full_name']
		username = response['data']['user']['username']
		is_private = response['data']['user']['is_private']
		biography = response['data']['user']['biography']
		follower_count= response['data']['user']['follower_count']
		following_count= response['data']['user']['following_count']
		media_count = response['data']['user']['media_count']
		profile_pic_url = response['data']['user']['hd_profile_pic_url_info']['url']
		return jsonify({'username':username,'full_name':full_name,'is_private':is_private,'profile_pic_url':profile_pic_url,'biography':biography,'follower':follower_count,'following':following_count,'posts':media_count},'\n')
		
	except:
		return {'status':'bad','message':'The Id Is Invaild Or Send request After 3 second '}

if __name__ == '__main__':
	app.run(debug=True)
