import os
# res for gif_maker
t_channel = "howMinskisbeautiful"  # format of info: str, just channel adress
parc_limit = 100 # butch limit of message from history
msg_limit = 800 # count of taking butches
pic_for_gif = 'rec_for_gif'
gif_storage_path = os.path.abspath(pic_for_gif)
os.makedirs(gif_storage_path, exist_ok=True)
need_save = False  # for test mod

# all buttons for work
from telethon.tl.custom import Button
list_of_buttons = [Button.inline('Make GIF', b'btn_gif_click'),  # gif_maker
                   Button.inline('Personal Planer', b'btn_pp_click')]

# secret config
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config.get('bot', 'bot_token')
api_id = int(config.get('bot', 'api_id'))
api_hash = config.get('bot', 'api_hash')
phone = config.get('bot', 'phone')
my_username = config.get('bot', 'my_username')
