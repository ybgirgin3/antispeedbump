import os
import shutil
from instabot import Bot
from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
import random
import time
from process_image import prep_and_fix
from json_funcker import json_funcker

username = 'antispeedbump_bmw_official'
password = 'yusufberkaygirgin2580'

#username = 'mental_huzur'
#password = 'manzaralar1234'


# https://github.com/basnijholt/instacron/blob/master/instacron.py#L378
def job():
    bot = Bot()

    bot.login(username = username, password = password)

    main_path = os.getcwd()
    #sent_path = os.path.join(main_path, 'araba_postları/sent_photos') # => send sent images to /tmp dir
    #unable_to_path = os.path.join(main_path, 'unable_to_post')
    post_path = os.path.join(main_path, 'araba_postları/fotolar')

    image = sorted([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    #image = 'Red lipstick is like a dangerous weapon... it is also same in the car... 💄🔴   owner @ramon_performance.jpg'
    full_image_path = os.path.join(post_path, image[0])
    print(f'chosen image: {full_image_path}')

    pic = prep_and_fix(full_image_path)

    full_im  = json_funcker(image[0])
    imagename = full_im[2]
    caption = os.path.splitext(imagename)[0]
    tags = full_im[3]
    upload = bot.upload_photo(pic, caption = """
{0}
💎 Follow @{1}
💎 Follow and join us


{2}

                    """.format(caption, username, tags))

    if upload:
        time.sleep(4)
        print('oldu amk!')
        #notif.send('{} isimli post başarılı bir şekilde instagramda paylaşıldı.'.format(image))
        #os.system(f'mv {full_image_path} {sent_path}')
        shutil.move('{}'.format(full_image_path), '/tmp')
        #sys.exit(0)
    else:
        #print('gönderilemedi.. yeniden başlıyor.')
        print('gönderilemedi.. tekrar deneyin')


    bot.logout()


if __name__ == '__main__':
    job()
