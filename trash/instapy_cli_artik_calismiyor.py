# link: https://pythonprogramming.altervista.org/post-on-instagram-from-the-computer-with-python-in-no-time/
from instapy_cli import client

username = 'mental_huzur'
password = 'manzaralar1234'
image = '/home/berkay/code/INSTAGRAM/antispeedbump/post1.jpg'
text = 'insta bot posting'

with client(username, password) as cli:
  cli.upload(image, text)
