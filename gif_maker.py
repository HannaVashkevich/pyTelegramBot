from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import public_resources as pr
import os
from PIL import Image, ImageDraw, ImageFont

# make connect for read history message
clbot = TelegramClient('clbot', pr.api_id, pr.api_hash).start()

async def main(ubot):
    gif_by_pic = []
    try:
        if pr.need_save:
            await grab_img()
        file_list_str = os.listdir(pr.pic_for_gif)
        file_list_int = []
        for f in file_list_str:
            try:
                file_list_int.append(int(f[:-4]))
            except:
                pass
        for p_name in sorted(file_list_int):
            # make gif in memory, read every pic in folder and appending future gif file
            path_pic_for_gif = os.path.join(pr.gif_storage_path, str(p_name) + '.jpg' )
            if os.path.isfile(path_pic_for_gif) and os.path.splitext(path_pic_for_gif)[1] == '.jpg':
                gif_by_pic.append(Image.open(path_pic_for_gif))
        print('31')
        # saving gif
        gif_by_pic[0].save(
            pr.gif_storage_path + '\\' + 'maked_gif.gif',
            save_all=True,
            append_images=gif_by_pic[1:],
            optimize=True,
            duration=500,
            loop=0
        )
        print('666')
    except Exception as e:
        print(e)
        await ubot.send_message(pr.my_username, ('unexpected error: ' + str(e)))


async def grab_img():
    offset_msg = 0  # start of grab
    total_messages = 0
    total_count_limit = pr.msg_limit  # limit of grabbing msg
    while True:
        posts = await clbot(GetHistoryRequest(
                                              peer=pr.t_channel,
                                              offset_id=offset_msg,
                                              offset_date=None,
                                              add_offset=0,
                                              limit=pr.parc_limit,
                                              max_id=0,
                                              min_id=0,
                                              hash=0))
        if not posts.messages:
            break
        mess = posts.messages
        for m in mess:
            total_messages = total_messages + 1
            if m.media:
                current_path = pr.gif_storage_path + '\\' + str(m.id) + '.jpg'
                if not os.path.isfile(current_path):
                    # get just new pic
                    bytes_pic = await clbot.download_media(m, bytes)
                    # read pic from message and get in memory
                    with open(current_path, "wb") as p:
                        # save pic in folder
                        p.write(bytes_pic)
                        p.close()
                    if m.message is not None:
                        i = Image.open(current_path)
                        # read jpg fom iteration, get message , drow txt on jpg
                        font = ImageFont.truetype("arial.ttf", 25)
                        drawer = ImageDraw.Draw(i)
                        drawer.text((10, 10), m.message, font=font, fill='black')
                        i.save(current_path)
                        i.close()
        offset_msg = mess[len(mess) - 1].id
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
