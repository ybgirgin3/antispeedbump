import os 
from instabot import Bot
import random
import time
#import resize_image


def job():
    bot = Bot() 

    bot.login(username = "antispeedbump_official", 
            password = "imthedeadreader") 

    # Recommended to put the photo 
    # you want to upload in the same 
    # directory where this Python code 
    # is located else you will have 
    # to provide full path for the photo 

    while True:
        post = random.choice([image for image in os.listdir('/home/berkay/Masaüstü/araba_postları/fotolar/') if os.path.splitext(image)[1] == '.jpg'])
        #resize_image(post)
        caption = os.path.splitext(post)[0]

        bot.upload_photo(post, 
            caption = """
            {}




            Don't forget to like, share, save and share with your friends to support us 💪🏻💪🏻💪🏻


    



            #bentley#ferrari #bentley_fan #maserati#automotive #rollsroyce #astonmartin #customcar #mulsanne #cadillac #newflyingspur #sportscar #luxurycar #rangerover#flyingspur #lamborghini #porche #jaguar #blacklist #carlove #cars #speed #forgiato#supercar #caroftheday#car #lexus #bmw#jeep
                    """.format(caption))
