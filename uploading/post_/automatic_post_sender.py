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

    bot.login(username = "antispeedbump_official", password = "yusufberkaygirgin2580")
    #bot.login(username = "mental_huzur", password = "manzaralar1234")

    main_path = '/home/berkay/code/INSTAGRAM/antispeedbump/post_uploading'
    sent_path = os.path.join(main_path, 'araba_postları/sent_photos')
    unable_to_path = os.path.join(main_path, 'unable_to_post')
    post_path = os.path.join(main_path, 'araba_postları/fotolar')

    image = random.choice([image for image in os.listdir(post_path) if os.path.splitext(image)[1] == '.jpg'])
    full_image_path = os.path.join(post_path, image)
    print(f'chosen image: {full_image_path}')

    pic = prep_and_fix(full_image_path)
    caption = os.path.splitext(image)[0]
    #tags = "#bmw #bmwm8 #m8 #m8competition #v8 #car #carsofinstagram"
    upload = bot.upload_photo(pic, caption = """
            {}


💪🏻 Tag a friend who need to see this
💪🏻 Don't forget to turn on notifications for more

Follow for more 👉🏻 @antispeedbump_official

                    """.format(caption))

    if upload:
        time.sleep(4)
        print('oldu amk!')
        notif.send('{} isimli post başarılı bir şekilde instagramda paylaşıldı.'.format(image))
        #os.system(f'mv {full_image_path} {sent_path}')
        shutil.move('{}'.format(full_image_path), sent_path)
        os.rmdir("config")
        #sys.exit(0)
    else:
        #shutil.move('{}'.format(full_image_path), unable_to_post)
        print('gönderilemedi.. yeniden başlıyor.')
        #os.system('/home/berkay/miniconda3/envs/antispeed/bin/python3 /home/berkay/code/INSTAGRAM/antispeedbump/post_uploading/automatic_post_sender.py')


    bot.logout()


if __name__ == '__main__':
    job()
