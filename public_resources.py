#secret config
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config.get('bot', 'bot_token')
api_id = int(config.get('bot', 'api_id'))
api_hash = config.get('bot', 'api_hash')
phone = config.get('bot', 'phone')
my_username = config.get('bot', 'my_username')

from telethon.tl.custom import Button
list_of_buttons = [Button.inline('Make GIF', b'btn_gif_click'),
                   Button.inline('Personal Planer', b'btn_pp_click')]