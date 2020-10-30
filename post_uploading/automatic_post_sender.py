import os 
from instabot import Bot
from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
import random
import time
from process_image import prep_and_fix

# https://github.com/basnijholt/instacron/blob/master/instacron.py#L378
def job():
    bot = Bot()

    #bot.login(username = "antispeedbump_official", password = "imthedeadreader")
    bot.login(username = "mental_huzur", password = "manzaralar1234")
    #image = 'merc.jpg'
    #image ='Pagani Heaven🏞.jpg'
    #image = os.path.join('/home/berkay/Masaüstü/araba_postları/fotolar/', )
    post_path = 'araba_postları/fotolar'
    image = random.choice([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    full_image_path = os.path.join(post_path, image)

    pic = prep_and_fix(full_image_path)
    caption = os.path.splitext(image)[0]
    tags = "#bentley #ferrari #bentley_fan #maserati #automotive #rollsroyce #astonmartin #customcar #mulsanne #cadillac #newflyingspur #sportscar #luxurycar #rangerover #flyingspur #lamborghini #porche #jaguar #blacklist #carlove #cars #speed #forgiato#supercar #caroftheday#car #lexus #bmw #jeep "
    upload = bot.upload_photo(pic, caption = """
            {}




   ❗❗❗ Don't forget to like, share, save and share with your friends to support us 💪🏻💪🏻💪🏻
   ❗❗❗ Don't forget to turn on notifications
   ❗❗❗ Follow for more 👉🏻 @antispeedbump_official



   {}
                    """.format(caption, tags))

    if upload:
        time.sleep(4)
        print('oldu amk!')
    else:
        print('olmadı amk')


    bot.logout()


if __name__ == '__main__':
    job()