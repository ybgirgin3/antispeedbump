"""
param1  :   path to video file
param2  :   caption
param3  :   thumbnail
"""

### NOTE:
## instagramdaki pixel sınırlamasından dolayı sadece yatay ekran boyutundaki videolar gönderilebiliyor
## youtube videolarından kestiğim videolarda şimdilik bir sıkıntı gözükmüyor

from instabot.api.api_video import get_video_info, configure_video, resize_video
from instabot import Bot

from thumbnailer import thumbnailed
import sys
from json_funcker import json_funcker
import os


"""
usern = 'mental_huzur'
passw = 'manzaralar2580'
"""
username = 'antispeedbump_bmw_official'
password = 'yusufberkaygirgin2580'


def video_job():
    # login
    bot = Bot()
    bot.login(username = username, password = password)

    # videoyu direk olarak tanımlamaktansa fotolardaki gibi
    # verdiğim pathten bulacak
    path = '/media/berkay/Elements/editlenecek_videolar/hazır_videolar/'

    # choose video
    video = sorted([video for video in os.listdir(path) if os.path.splitext(video)[1] == '.mp4'])

    # show chosen video
    choosen_vid_path = os.path.join(path, video[0])
    print(f'choosen video: {choosen_vid_path}')

    # caption
    full_vid = json_funcker(video[0])
    videoname = full_vid[2]
    caption = os.path.splitext(videoname)[0]

    # tags
    tags = full_vid[3]

    # thumbnail
    thumb = thumbnailed(choosen_vid_path)
    #video = resize_video(video)
    print(f'choosen vid: {video}')
    upload_vid = bot.upload_video(choosen_vid_path, caption= """
{0}
Follow for more 👉🏻 @{1}

💪🏻Don't forget to like save and share with your friends
💪🏻Don't forget to turn on notifications
✉ Dm for credit


{2}

    """.format(caption, username, tags), thumbnail=thumb)

    if upload_vid:
        print('oldu amk')
    else:
        print('olmadı yine aq')



video_job()
