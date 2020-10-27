import os
import time 
from instabot import Bot 


bot = Bot() 
bot.login(username = "mental_huzur", 
		password = "manzaralar1234") 

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have 
# to provide full path for the photo 

# find images and get their names a list
post_path = '/home/berkay/code/INSTAGRAM/antispeedbump/posts'
posts = []
for post in os.listdir(post_path):
  posts.append(post)



for post in posts:
  bot.upload_photo(post,
                  caption = os.path.splitext(post)[0]) 
  time.sleep(2)

