# link: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
import os
import ntpath
from threading import Thread
from net_check import Net

# kendi modülüm
from actions_ import follow_, comment_, like_, session
from instapy import smart_run

"""
# kullanıcı adı ve şifreyi gir sisteme
session = InstaPy(username='mental_huzur',
                  password='manzaralar1234', 
                  headless_browser=True
                  )
# giriş yap
session.login()
"""

# dosya yolları
#follow_tag_file = '/home/berkay/code/INSTAGRAM/antispeedbump/follow_tag_file.txt'
follow_tag_file_path = os.getcwd()+'/text_files/follow_tag_file.txt'
like_tag_file_path = os.getcwd()+'/text_files/like_tag_file.txt'




# kullanıcıları takip etmek için tagler lazım o tagleri liste olarak
# almam gerekiyor
# tag listesini okuma fonksiyonu içine yolla,
# sonra da direk olarak follow_ içine

# kesinlikle multithread gerekli
# çünkü follow işini bitirmeden like işlemine geçmiyor
while Net:
  try:
    with smart_run(session, threaded=True):
        Thread(target = follow_(follow_tag_file_path)).start()
        Thread(target = like_(like_tag_file_path)).start()
      
        #session.end(threaded_session=True)
  except Exception as e:
    raise('Timeout Error')
