from telethon import TelegramClient, events
import gif_maker
import public_resources as pr

ubot = TelegramClient('ubot', pr.api_id, pr.api_hash).start(bot_token=pr.bot_token)


@ubot.on(events.NewMessage(pattern='/start'))
async def welcome(event):
    await event.reply("Hello, i'm bot for personal Hanna's needs", buttons=pr.list_of_buttons)


@ubot.on(events.CallbackQuery(data=b'btn_gif_click'))
async def gif_make(event):
    await gif_maker.main(ubot)

ubot.run_until_disconnected()
