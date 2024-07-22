import os
os.system('pip install telethon')
os.system('pip install telebot')
import telebot
from telebot import types
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import random
import requests
from datetime import datetime
from telethon.tl.functions.account import CheckUsernameRequest
from telethon import errors, functions
import os

status = False
good, ban, bad, ftag, takentele = 0, 0, 0, 0, 0

bot = telebot.TeleBot('6882490925:AAE-S1M79DcEKPQvRZmc2ytl_xzk_yT-5Cc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    start_button = types.InlineKeyboardButton("- بدء .", callback_data='start_fishing')
    stop_button = types.InlineKeyboardButton("- ايقاف .", callback_data='stop_fishing')
    developer_button = types.InlineKeyboardButton("- المطور .", url='https://t.me/cc_02')
    stus = types.InlineKeyboardButton("- حالة الصيد .", callback_data='statun')
    add_session = types.InlineKeyboardButton("- اضف سيشن .", callback_data='add_session')
    check_all = types.InlineKeyboardButton("- فحص جميع السيشنات .", callback_data='check_all')
    markup.add(start_button, stop_button, add_session,check_all,stus, developer_button)
    bot.send_message(message.chat.id, "اختر أحد الخيارات:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global status ,good, ban, bad, ftag, takentele
    if call.data == 'add_session':
        bot.send_message(call.message.chat.id, "- ارسل السيشن الان .")
        bot.register_next_step_handler(call.message, check_session)
    elif call.data == 'start_fishing':
        try:
           tty=open('session_true.txt','r').read().strip().split('\n')
           if len(tty) >= 1:
           	        if status:
           	        	bot.send_message(call.message.chat.id, '- الصيد مفعل بالفعل .')
           	        else:
           	        	status = True
           	        	bot.send_message(call.message.chat.id, '- تم بدء الصيد')
           	        	asyncio.run(start_fishing(call))
        except FileNotFoundError:
           	bot.send_message(call.message.chat.id, '- يرجى فحص السيشنات ليمكنك استخدام هذا الامر .')
    elif call.data == 'stop_fishing':
        if status:
            good, ban, bad, ftag, takentele=0,0,0,0,0
            status = False
            bot.send_message(call.message.chat.id, '- تم ايقاف الصيد .')
        else:
            bot.send_message(call.message.chat.id, '- الصيد متوقف بالفعل .')
    elif call.data == 'statun':
    	bot.send_message(call.message.chat.id,f'- Welcome :\n- Good : {good}\n- Bad : {takentele}\n- Available in Fragment : {ftag}\n- Ban : {ban}\n- Other : {bad}')
    elif call.data == 'check_all':
    	asyncio.run(checks(call)) 
    			
async def start_fishing(call):
    global status
    file = open('session_true.txt', 'r').read().strip().split('\n')
    session = random.choice(file)
    client = await clienx(session)
    while status:
        await all(client, call)
async def checks(call):
    	try:
    		try:
    			os.remove('session_true.txt')
    		except FileNotFoundError:
    			pass
    		file=open('session.txt','r').read().strip().split('\n')
    		for session in file:
	    		client = TelegramClient(StringSession(session), 25635928, '6e49a338bcf4c3406afdb0ce9a2892e1')
	    		await client.connect()
	    		if  await client.is_user_authorized():
	    			with open('session_true.txt', 'a') as file:
	    				file.write(f'{session}\n')
	    				await client.disconnect()
	    				bot.send_message(call.message.chat.id, f'- شغال : {session} .')
	
	    		else:
	    			bot.send_message(call.message.chat.id, f'- خطا في السيشن : {session} .')
    	except FileNotFoundError:
    		bot.send_message(call.message.chat.id,'- اضف سيشنات ليمكنك استخدام هذا الخيار .')

async def clienx(session):
    client = TelegramClient(StringSession(session), 25635928, '6e49a338bcf4c3406afdb0ce9a2892e1')
    await client.start()
    return client

async def all(client, call):
    global good, ban, bad, ftag, takentele
    username = gen()
    frag = fragment(username)
    if frag == True:
        che =  await check(client,username)
        print(che)
        if che == True:
            good += 1
            bot.send_message(call.message.chat.id, f'good : {username}')
            clio = await climed(client, username)
            if clio == True:
                bot.send_message(call.message.chat.id, f'Done Claimd : {username}')
        elif che == False:
            bad += 1
        elif str(che) == 'ban':
            ban += 1
    elif str(frag) == 'is taken':
        takentele += 1
    else:
        ftag += 1

async def climed(client, username):
    result = await client(functions.channels.CreateChannelRequest(
        title=f'Done Claimd :  {username} ',
        about=f'by : @cc_02', megagroup=False))
    try:
        await client(functions.channels.UpdateUsernameRequest(
            channel=result.chats[0],
            username=username))
        await client.send_message(username, f'- Done Claimd The Username : {username}\n- Date : {datetime.now().strftime("%H:%M:%S")}\n- By : @cc_02')
        return True
    except Exception as e:
        await client.send_message('me', f'- Error   : {e} .')
    return False

def gen():
    a = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    b = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    use1=a+b*7
    use2=a+b*6
    use3=a*3+b+b+a*2
    return random.choice([use1,use2,use3])



async def check(client,username):
		try:
			check = await client(CheckUsernameRequest(username))
			print(check)
			if check :
				return True
			else:
				return False
		except errors.rpcbaseerrors.BadRequestError:
			return 'ban'
def fragment(username):
	url = f"https://fragment.com/username/{username}"
	headers = {
		'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
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

def check_session(message):
    session = message.text
    try:
        file = open('session.txt', 'r').read().strip().split('\n')
        if session in file:
            bot.send_message(message.chat.id, '- هذا السيشن موجود بالفعل .')
        else:
            asyncio.run(add_session1(message, session))
    except FileNotFoundError:
        asyncio.run(add_session1(message, session))

async def add_session1(message, session):
    try:
        client = TelegramClient(StringSession(session), 25635928, '6e49a338bcf4c3406afdb0ce9a2892e1')
        await client.connect()
        if await client.is_user_authorized():
            with open('session.txt', 'a') as file:
                file.write(f'{session}\n')
            await client.disconnect()
            bot.reply_to(message, '- تم الحفظ . ')
        else:
            bot.send_message(message.chat.id, '- خطا في السيشن .')
    except:
         bot.reply_to(message, f'- خطا في تنسيق السيشن .')

bot.polling()
