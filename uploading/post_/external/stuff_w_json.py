import os 
import shutil
#from instabot import Bot
#from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
import random
import time
from process_image import prep_and_fix
#from notify_run import Notify
#notif = Notify()


# tag dictleri
M =  {

  "M8": "#bmw #bmwm8 #m8 #m8competition #v8 #car #carsofinstagram",
  "M6": "#bmw #bmwm6 #m6 #v8 #m6grandcoupe #m6coupe #car #carsofinstagram #twinturbo",
  "M5": "#bmw #bmwm5 #m5 #v8 #m5competition #car #carsofinstagram #twinturbo #m5lci",
  "M4": "#bmw #bmwm4 #m4 #S55 #convertible #m4competition #car #carsofinstagram #twinturbo #m4csl",
  "M3": "#bmw #bmwm3 #m3 #S55 #v8 #e92 #f82 #g20 #m3competition #twinturbo #m3csl",
  "M2": "#bmw #bmwm2 #m2 #S55 #f87 #turbocharged #twinturbo #m2csl #m3competition #m2csl"
}


X =  {
  "X3": "#bmw #bmwx3 #x3 #x3m #x3mcompetition #S55 #car #carsofinstagram #turbocharged",
  "X5": "#bmw #bmwx5 #x5 #x5m #x5mcompetition #v8 #twinturbo #turbocharged #suv #carsofinstagram",
  "X6": "#bmw #bmwx6 #x6 #x6m #x6mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged",
  "X7": "#bmw #bmwx7 #x7 #x7m50i #x7mcompetition #v8 #twinturbo #turbocharged #suv #twinturbocharged"
}


def json_funcker(model):
    sp = model.split(",")
    tag = None
    if sp[1] == 'M':
        if sp[2] in M:
            tag =  M[sp[2]]

    elif sp[1] == 'X':
        if sp[2] in X:
            tag = X[sp[2]]

    # ret = "M", "M6", "white", "#bmwm6"
    ret = sp[1], sp[2], sp[3], tag
    return ret


# https://github.com/basnijholt/instacron/blob/master/instacron.py#L378
def job():
    #bot = Bot()

    #bot.login(username = "antispeedbump_bmw_official", password = "yusufberkaygirgin2580")
    #bot.login(username = "mental_huzur", password = "manzaralar1234")

    #main_path = '/home/berkay/code/INSTAGRAM/antispeedbump/uploading/post_/araba_postları/fotolar/'
    main_path = os.getcwd()
    sent_path = os.path.join(main_path, 'araba_postları/sent_photos')
    #unable_to_path = os.path.join(main_path, 'unable_to_post')
    post_path = os.path.join(main_path, 'araba_postları/fotolar')

    image = sorted([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    #image = "1,X,X5,Looks like crazy things about to happen.. Color of the Devil 😈.jpg"
    full_image_path = os.path.join(post_path, image[0])
    #print(type(image[0]))
    #print(image[0])
    #print(f'chosen image: {full_image_path}')

    #pic = prep_and_fix(full_image_path)

    # after funcking
    full_im  = json_funcker(image[0])
    imagename = full_im[2]
    caption = os.path.splitext(imagename)[0]
    tags = full_im[3]

    print(f'caption: {caption}')
    print(f'tags: {tags}')


job()

