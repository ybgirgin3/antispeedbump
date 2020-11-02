import os 
import shutil
from instabot import Bot
from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
import random
import time
from process_image import prep_and_fix
#from notify_run import Notify
#notif = Notify()


# tag dictleri
M =  {
    "regular": "#bmw #car #luxury #sports #carsofinstagram #m4 #m3 #m2 #1m #7 #m6 #m8",
    "eski_model": "#bmw #bmw2002 #classical #nostalgia #old #oldcar #2002 #carsofinstagram",
    "7_series": "#bmw #m #7 #The7 #7Series #7series #bmw7 #v12 #v8 #luxury",
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

username = 'antispeedbump_bmw_official'
password = 'yusufberkaygirgin2580'

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
    bot = Bot()

    bot.login(username = username, password = password)
    #bot.login(username = "mental_huzur", password = "manzaralar1234")

    #main_path = '/home/berkay/code/INSTAGRAM/antispeedbump/uploading/post_/araba_postları/fotolar/'
    main_path = os.getcwd()
    sent_path = os.path.join(main_path, 'araba_postları/sent_photos')
    #unable_to_path = os.path.join(main_path, 'unable_to_post')
    post_path = os.path.join(main_path, 'araba_postları/fotolar')

    image = sorted([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    full_image_path = os.path.join(post_path, image[0])
    print(f'chosen image: {full_image_path}')

    pic = prep_and_fix(full_image_path)

    full_im  = json_funcker(image[0])
    imagename = full_im[2]
    caption = os.path.splitext(imagename)[0]
    tags = full_im[3]
    upload = bot.upload_photo(pic, caption = """
            {0}


💪🏻 Tag a friend who need to see this
💪🏻 Don't forget to like comment and share with your friends
💪🏻 Don't forget to turn on notifications for more

Follow for more 👉🏻 @{1}
Follow for more 👉🏻 @{1}

{2}

                    """.format(caption, username, tags))

    if upload:
        time.sleep(4)
        print('oldu amk!')
        #notif.send('{} isimli post başarılı bir şekilde instagramda paylaşıldı.'.format(image))
        #os.system(f'mv {full_image_path} {sent_path}')
        shutil.move('{}'.format(full_image_path), sent_path)
        #sys.exit(0)
    else:
        #shutil.move('{}'.format(full_image_path), unable_to_post)
        print('gönderilemedi.. yeniden başlıyor.')
        #os.system('/home/berkay/miniconda3/envs/antispeed/bin/python3 /home/berkay/code/INSTAGRAM/antispeedbump/post_uploading/automatic_post_sender.py')


    bot.logout()


if __name__ == '__main__':
    job()
