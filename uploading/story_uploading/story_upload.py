from instabot import Bot
from instabot.api.api_story import configure_story

USERNAME = 'mental_huzur'
PASSWORD = 'manzaralar1234'

def story_job():
	bot = Bot()
	bot.login(username = USERNAME, password = PASSWORD)

	image = 'm5.jpeg'
	print(f'choosen image: {image}')

	pic = configure_story(upload_id=1, photo=image)

	upload = bot.upload_story_photo(pic)


	if upload:
		print('oldu amk')
	else:
		print('olmadı amk')

story_job()
