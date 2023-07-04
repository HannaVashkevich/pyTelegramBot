from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import public_resources as pr
import datetime

clbot = TelegramClient('clbot', pr.api_id, pr.api_hash).start()
async def main(ubot):
    await ubot.send_message(pr.my_username, 'lets fun')

    try:
        mess = await clbot(GetHistoryRequest(
                                            peer=pr.t_channel,
                                            limit=pr.parc_limit,
                                            offset_id=42,
                                            offset_date=datetime.datetime(2018, 6, 25),
                                            add_offset=0,
                                            max_id=0,
                                            min_id=0,
                                            hash=-12398745604826))
        print('ttt')
        await ubot.send_message(pr.my_username, mess.stringify())
    except Exception as e:
            await ubot.send_message(pr.my_username, ('unexpected error: ' + str(e)))

