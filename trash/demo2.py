import os
import time 
import random
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


#print(os.listdir(post_path)) -> returns list
post = random.choice(os.listdir(post_path))
bot.upload_photo(post, caption='hi bot 2')
os.replace(post_path, post_path+'/sent')

