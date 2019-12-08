import requests
import time
import os
from rocketchat_API.rocketchat import RocketChat                 

# Rocketchat configuration
server_url = os.environ['ROCKET_URL']
channel_id = os.environ['ROCKET_CHANNEL_ID']
acronym = os.environ['ROCKET_LOGIN']
password = os.environ['ROCKET_PASSWORD']

# Telegram configuration
bot_token = os.environ['TELEGRAM_BOT_TOKEN']
bot_chatID = os.environ['TELEGRAM_CHANNEL_ID']

# Conection with Rocket.Chat
rocket = RocketChat(acronym, password, server_url=server_url)

# Read last message in channel
data = rocket.channels_history(channel_id, count=1).json()
old_message = data['messages'][0]['msg']

while True:
    data = rocket.channels_history(channel_id, count=1).json()
    message = data['messages'][0]['msg']

    # New message detected
    if old_message != message:
        # Send message to Telegram
        name = username = data['messages'][0]['u']['name']
        username = data['messages'][0]['u']['username']   
        message_to_telegram = name + " (" + username + ")"+ ": " + message
        print ("A new message to Telegram will be sent: \n" + message_to_telegram)
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message_to_telegram
        response = requests.get(send_text)
    
    old_message = message  

    # Wait before take a look for new messages 
    time.sleep(2)


