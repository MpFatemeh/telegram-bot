import sys
import time
import telepot
from telepot.loop import MessageLoop

TOKEN = '' #bot token
CHANNEL = '' #channel id
bot = telepot.Bot(TOKEN)
#print(bot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'document':
        file_id = msg['document']['file_id']
        bot.sendDocument(chat_id=CHANNEL,document=file_id, caption='')
        print(file_id)

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)