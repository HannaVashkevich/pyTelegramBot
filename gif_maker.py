from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import public_resources as pr
import datetime
import os
from PIL import Image, ImageDraw, ImageFont

clbot = TelegramClient('clbot', pr.api_id, pr.api_hash).start() #make connect for read history message
async def main(ubot):
    await ubot.send_message(pr.my_username, 'lets fun')
    gif_by_pic = []
    try:
        mess = await clbot(GetHistoryRequest(
                                            peer=pr.t_channel,
                                            limit=pr.parc_limit,
                                            offset_id=800,
                                            offset_date=datetime.datetime(2018, 6, 25),
                                            add_offset=0,
                                            max_id=0,
                                            min_id=0,
                                            hash=-12398745604826))
        for m in mess.messages:
            print(str(m.id))
            if m.media:
                current_path = pr.gif_storage_path + '\\' + str(m.id) + '.jpg'
                if not os.path.isfile(current_path): #get just new pic
                    bytes_pic = await clbot.download_media(m, bytes)  # read pic from message and get in memory
                    with open(current_path, "wb") as p: #save pic in folder
                        p.write(bytes_pic)
                        p.close()
                    if m.message is not None:
                        i = Image.open(current_path) # read jpg fom iteration, get message , drow txt on jpg
                        font = ImageFont.truetype("arial.ttf", 25)
                        drawer = ImageDraw.Draw(i)
                        drawer.text((10, 10), m.message, font=font, fill='black')
                        i.save(current_path)
                        i.close()

        await ubot.send_message(pr.my_username, 'i')

        for p_name in sorted(os.listdir(pr.pic_for_gif)): #make gif in memory, read every pic in folder and appendin future gif file
            path_pic_for_gif = os.path.join(pr.gif_storage_path, p_name)
            if os.path.isfile(path_pic_for_gif) and os.path.splitext(path_pic_for_gif)[1] == '.jpg':
                gif_by_pic.append(Image.open(path_pic_for_gif))
        gif_by_pic[0].save( #saving gif
            pr.gif_storage_path +'\\'+ 'maked_gif.gif',
            save_all=True,
            append_images=gif_by_pic[1:],
            optimize=True,
            duration=500,
            loop=0
        )

    except Exception as e:
            await ubot.send_message(pr.my_username, ('unexpected error: ' + str(e)))
