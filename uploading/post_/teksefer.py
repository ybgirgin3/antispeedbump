import os 
import shutil
from instabot import Bot
from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
import random
import time
from process_image import prep_and_fix
from notify_run import Notify
notif = Notify()


# https://github.com/basnijholt/instacron/blob/master/instacron.py#L378
def job():
    bot = Bot()

    bot.login(username = "antispeedbump_bmw_official", password = "yusufberkaygirgin2580")
    #bot.login(username = "mental_huzur", password = "manzaralar1234")

    main_path = '/home/berkay/code/INSTAGRAM/antispeedbump/post_uploading'
    sent_path = os.path.join(main_path, 'araba_postları/sent_photos')
    unable_to_path = os.path.join(main_path, 'unable_to_post')
    post_path = os.path.join(main_path, 'araba_postları/fotolar')

    #image = random.choice([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    #image = 'BMW M5  Fire Orange🧡🍊.jpeg'
    image = 'Red lipstick is like a dangerous weapon... it is also same in the car... 💄🔴   owner @ramon_performance.jpg'
    full_image_path = os.path.join(post_path, image)
    print(f'chosen image: {full_image_path}')

    pic = prep_and_fix(full_image_path)
    caption = os.path.splitext(image)[0]
    tags = "#bmw #bmwm3 #bmwm4 #bmwlife #bmwm3drift #bmwi8 #bmwm5 #bmwx5 #bmwm #bmwlove #bmwx3 #bmw4series #bmw335i #bmwrepost #bmwgram #bmwnation #bmw #bmwlover #bmwlife #bmwm #m2 #m3 #m4 #m5 #bmwclup #bmwmpower #bmwgram #bmwmperformance #bmwmotorsport #bmwfan #bmwmodification #bmwlove #bmwmnation #bmwnation #v8 "
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
        notif.send('{} isimli post başarılı bir şekilde instagramda paylaşıldı.'.format(image))
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
