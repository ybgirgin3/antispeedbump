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
import subprocess
import time
import shutil



def video_job(path, video):
    # login
    bot = Bot()
    bot.login(username = username, password = password)

    # videoyu direk olarak tanımlamaktansa fotolardaki gibi
    # verdiğim pathten bulacak

    
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
    #print(f'choosen vid: {video}')
    upload_vid = bot.upload_video(choosen_vid_path, caption= """
{0}

💎 Follow @{1}
💎 Follow and join us

{2}

    """.format(caption, username, tags), thumbnail=thumb)

    if upload_vid:
        print('oldu amk')
        shutil.move('{}'.format(choosen_vid_path), '/tmp')
    else:
        print('olmadı yine aq')




#path = '/media/berkay/Elements/editlenecek_videolar/tasinmislar'
path = '/media/berkay/Elements/editlenecek2/tasinmislar'
# choose video
video = sorted([video for video in os.listdir(path) if os.path.splitext(video)[1] == '.mp4'])
if len(video) == 0:
    subprocess.run(['/home/berkay/miniconda3/envs/antispeed/bin/python', '/home/berkay/code/SocialMedia/antispeedbump/uploading/post_/prep_video.py'])
    time.sleep(2)


video_job(path, video)
