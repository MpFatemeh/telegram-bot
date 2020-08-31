import sys
import time
import telepot

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop

numbers={}
counter=0
TOKEN = '' #bot token
bot = telepot.Bot(TOKEN)

def handle(msg):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='+', callback_data='+')
													,InlineKeyboardButton(text='-', callback_data='-')]
													,[InlineKeyboardButton(text='*', callback_data='*')
													,InlineKeyboardButton(text='/', callback_data='/')]])
    content_type, chat_type, chat_id = telepot.glance(msg)

    global counter
    if msg['text'] == '/start':
    	bot.sendMessage(chat_id, 'Welcome to our learning project, Send your first number:')
    	counter=0
    	return
    numbers[counter]=int(msg['text'])
    if counter==0:
    	bot.sendMessage(chat_id,'Send your second number...')
    	counter+=1
    elif counter==1:
    	bot.sendMessage(chat_id,'Select Your Operator...',reply_markup=keyboard)
    	counter+=1

def on_callback_query(msg):
	global counter
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	chat_id = msg['from']['id']
	if query_data=='+':
       	   counter=0
       	   bot.sendMessage(chat_id,'your result: ' +  str(numbers[0]) + '+' + str(numbers[1]) + '=' + str(numbers[0]+numbers[1]))
	if query_data=='-':
       	   counter=0
       	   bot.sendMessage(chat_id,'your result: ' +  str(numbers[0]) + '-' + str(numbers[1]) + '=' + str(numbers[0]-numbers[1]))
	if query_data=='/':
       	   counter=0
       	   bot.sendMessage(chat_id,'your result: ' +  str(numbers[0]) + '/' + str(numbers[1]) + '=' + str(numbers[0]/numbers[1]))
	if query_data=='*':
       	   counter=0
       	   bot.sendMessage(chat_id,'your result: ' +  str(numbers[0]) + '*' + str(numbers[1]) + '=' + str(numbers[0]*numbers[1]))

def answerCallbackQuery(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
	p = _strip(locals())
	return self._api_request('answerCallbackQuery', _rectify(p))

       	   
MessageLoop(bot, {'chat': handle,'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)