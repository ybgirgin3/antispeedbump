from instabot import Bot
from instabot.api.api_story import configure_story


def story_job():

    # login account
    bot = Bot()
    bot.login(username = username, password =  password)

    # image defining
    image = 'm5.jpeg'
    print(f'choosen image: {image}')

    """
    @param1 :   photo
    @param2 :   upload_id=None -> if None -> bot configures by itself

    """
    upload = bot.upload_story_photo(photo = image, upload_id = None)

    if upload:
        print('oldu amk')
    else:
        print('olmadı amk')


story_job()
