import os 
from instabot import Bot
import random
import time
#import resize_image


def job():
    bot = Bot() 

    bot.login(username = "mental_huzur", 
            password = "manzaralar1234") 

    # Recommended to put the photo 
    # you want to upload in the same 
    # directory where this Python code 
    # is located else you will have 
    # to provide full path for the photo 

    while True:
        post = random.choice([image for image in os.listdir('.') if os.path.splitext(image)[1] == '.jpg'])
        #resize_image(post)
        caption = os.path.splitext(post)[0]

        bot.upload_photo(post, 
            caption = """
            {}


            #bot #python #automation

                    """.format(caption))
