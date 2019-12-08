import requests
import time
from getpass import getpass
from rocketchat_API.rocketchat import RocketChat
from pprint import pprint                       

# Rocketchat configuration
server_url = str(input("Rocketchar server URL: "))
channel_id = str(input("Rocketchar channel ID: "))
acronym = str(input("Set your acronym: "))
password = getpass()

# Telegram configuration
bot_token = str(input("Telegram BOT token: "))
bot_chatID = str(input("Telegram Chat ID: "))

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
    time.sleep(1)


