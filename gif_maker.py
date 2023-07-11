from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import public_resources as pr
import datetime
import os
from PIL import Image
clbot = TelegramClient('clbot', pr.api_id, pr.api_hash).start()
async def main(ubot):
    await ubot.send_message(pr.my_username, 'lets fun')
    gif_by_pic = []
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

        for m in mess.messages:
            blob = await clbot.download_media(m, bytes)
            with open(pr.gif_storage_path + '\\' + str(m.id) + '.jpg', "wb") as p:
                p.write(blob)
        await ubot.send_message(pr.my_username, 'i')


        for p_name in os.listdir(pr.pic_for_gif):
            path_pic_for_gif = os.path.join(pr.pic_for_gif, p_name)
            if os.path.isfile(path_pic_for_gif):
                gif_by_pic.append(Image.open(path_pic_for_gif))
        print('1111')
        gif_by_pic[0].save(
            pr.pic_for_gif+'\\'+ 'maked_gif.gif',
            save_all=True,
            append_images=gif_by_pic[1:],
            optimize=True,
            duration=500,
            loop=0
        )

    except Exception as e:
            await ubot.send_message(pr.my_username, ('unexpected error: ' + str(e)))
