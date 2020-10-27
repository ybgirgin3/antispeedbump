# link: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
from instapy import InstaPy

# kendi modülüm
from actions_ import follow_, comment_, like_

# kullanıcı adı ve şifreyi gir sisteme
session = InstaPy(username='mental_huzur',
                  password='manzaralar1234', 
                  headless_browser=True
                  )
# giriş yap
session.login()


# dosya yolları
tag_file = '/home/berkay/code/INSTAGRAM/antispeedbump/tags_for_following.txt'


def read_from_file(filename):
	with(filename, 'r') as tf:
		tags = tf.read().splitlines()
		f.close()
	return tags



# kullanıcıları takip etmek için tagler lazım o tagleri liste olarak
# almam gerekiyor
# tag listesini okuma fonksiyonu içine yolla,
# sonra da direk olarak follow_ içine
follow_(read_from_file(tag_file))