"""
param1  :   path to video file
param2  :   caption
param3  :   thumbnail
"""



from instabot.api.api_video import get_video_info, configure_video, resize_video
from instabot import Bot

from thumbnailer import thumbnailed
import sys


"""
usern = 'mental_huzur'
passw = 'manzaralar2580'
"""
usern = 'antispeedbump_bmw_official'
passw = 'yusufberkaygirgin2580'


def video_job():
    # login
    bot = Bot()
    bot.login(username = usern, password = passw)

    video = sys.argv[1]
    thumb = thumbnailed(video)
    print(f'choosen vid: {video}')
    upload_vid = bot.upload_video(video, caption='BMW M5 take off loud sound', thumbnail=thumb)

    if upload_vid:
        print('oldu amk')
    else:
        print('olmadı yine aq')



video_job()
