from instabot import Bot 


bot = Bot() 

bot.login(username = "mental_huzur", 
		password = "manzaralar1234") 

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have 
# to provide full path for the photo 
bot.upload_photo("post3.jpg", 
				caption ="hello bot") 

