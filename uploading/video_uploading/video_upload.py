from instabot.api.api_video import get_video_info, configure_video, resize_video
from instabot import Bot

usern = 'mental_huzur'
passw = 'manzaralar1234'


def video_job():
    bot = Bot()
    bot.login(username = usern, password = passw)

    video = 'vid.mp4'
    print(f'choosen vid: {video}')
    #info = get_video_info(video)
    #print(f'about video file: {info}')
    upload_vid = bot.upload_video(video)

    if upload_vid:
        print('oldu amk')
    else:
        print('olmadı yine aq')



video_job()
