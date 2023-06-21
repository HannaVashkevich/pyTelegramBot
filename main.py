from telethon import TelegramClient, events
import public_resources as pr

bot = TelegramClient('bot', pr.api_id, pr.api_hash).start(bot_token=pr.bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def welcome(event):
    print('aaa')
    await event.reply("Hello, i'm bot for personal Hanna's needs", buttons=pr.list_of_buttons)


@bot.on(events.CallbackQuery(data=b'btn_gif_click'))
async def gif_make(event):
    pass


if __name__ == '__main__':
    bot.run_until_disconnected()
