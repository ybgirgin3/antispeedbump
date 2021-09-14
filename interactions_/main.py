# link: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
import os
import sys
import ntpath
import time
from threading import Thread
from net_check import Net

# kendi modülüm
from actions_ import follow_, like_and_comment, session, unfollowing
from actions2 import job, unf
from instapy import smart_run



# dosya yolları
#follow_tag_file = '/home/berkay/code/INSTAGRAM/antispeedbump/follow_tag_file.txt'
follow_tag_file_path = os.getcwd()+'/text_files/follow_tag_file.txt'
like_tag_file_path = os.getcwd()+'/text_files/like_tag_file.txt'
#comment_path = os.getcwd()+'/text_files/comments.txt'
comment_path = [
				u"cool!! 💯 Don't forget to checkout my account",
				u"Awesome 💯 Don't forget to checkout my account",
				u"Great Photo!! 😍😍😍 Don't forget to checkout my account",
				u"This post is 🔥 !! Don't forget to checkout my account",
				u"I like it 😍😍😍 Don't forget to checkout my account",
				]

big_accounts_path = os.getcwd()+'/text_files/big_accounts.txt'




# kullanıcıları takip etmek için tagler lazım o tagleri liste olarak
# almam gerekiyor
# tag listesini okuma fonksiyonu içine yolla,
# sonra da direk olarak follow_ içine

# kesinlikle multithread gerekli
# çünkü follow işini bitirmeden like işlemine geçmiyor

with smart_run(session, threaded=True):
    #job(big_accounts=None, comments_list=comment_path)
    unf()

	#Thread(target = follow_(follow_tag_file_path, big_accounts=big_accounts_path)).start()
	#Thread(target = follow_(big_accounts=big_accounts_path)).start()
	#print('takip işi bitti 15 dk bekleme süresi başladı')
	#time.sleep(900)

	#Thread(target = like_and_comment(like_tag_file_path, comment_path)).start()
	#print('like işi bitti 15 dk bekleme süresi başladı')
	#time.sleep(900)

	#print('unfollowing başlıyor')
	#Thread(target = unfollowing()).start()
