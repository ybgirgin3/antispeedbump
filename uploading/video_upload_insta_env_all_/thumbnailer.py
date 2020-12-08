import cv2
import sys
import random
import os

#video = 'post.mp4'
#video = 'post2.mp4'

# tqdm init
# total kısmına toplam frame sayısını yazmamız lazım

def dir_control():
    # thumbnaillerin kaydedileceği klasör
    target_folder = os.getcwd()+'/frames'
    if os.path.isdir(target_folder):
        # boş mu dolu mu diye bak
        ret = [frame for frame in os.listdir(target_folder)]
        if len(ret) > 0:
            to_remove = [os.path.join(target_folder, f) for f in os.listdir(target_folder)]
            for f in to_remove:
                os.remove(f)
        else: pass

    else:
        os.mkdir('frames')
        target_folder = os.getcwd()+'/frames'

    return target_folder


def thumbnailed(video):
    target_folder = dir_control()
    # extract of the video and save it to a folder
    vid = cv2.VideoCapture(video)
    success, image = vid.read()
    count = 0 
    while success:
        cv2.imwrite("{0}/frame{1}.jpg".format(target_folder, count), image)
        success, image = vid.read()
        #print('read a new frame: {}', success)
        sys.stdout.write('Image writed: {0}/frame{1}'.format(target_folder, count) + '\r')
        sys.stdout.flush()
        count += 1

    img = random.choice([frame for frame in os.listdir(target_folder)])
    return os.path.join(target_folder, img)

##read_vid(video)
