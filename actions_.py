# follow_tag_list: liste olmalı - main.py'dan gönderilecek
from instapy import InstaPy
from inf import USERNAME, PASSWORD
import random
import time


wait_time = random.randint(60, 900)

# kullanıcı adı ve şifreyi gir sisteme
session = InstaPy(username=USERNAME,
                  password=PASSWORD, 
                  headless_browser=False,
                  #disable_image_load=True,
                  )
# giriş yap
session.login()



# durumları aktif et

# banlanmamak için supervisor aktif et
# limitler ile ilgili bilginin alındığı link: https://taplink.at/en/blog/instagram_follow_unfollow_limits_and_other_restrictions_2020.html#:~:text=In%202020%2C%20users%20are%20allowed,more%20freedom%20in%20this%20regard.
session.set_quota_supervisor(enabled=True,
                             sleep_after=["likes", "comments_d", "follows_h", "unfollows_h", "server_calls_h"],
                             sleepyhead=True, 
                             stochastic_flow=True, 
                             notify_me=True,
                             peak_likes_hourly=30,
                             peak_likes_daily=500,
                             peak_comments_hourly=21,
                             peak_comments_daily=240,
                             peak_follows_hourly=20,
                             peak_follows_daily=200,
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=200,
                             peak_server_calls_hourly=500,
                             peak_server_calls_daily=4700)

# bot aktivitesini instagramdan saklamak için belirli süreleri içerisinde bu işlemleri tekrarla
session.set_action_delays(enabled=True,
                          like=30,
                          comment=29,
                          follow=71,
                          unfollow=28,
                          story=10,
                          randomize=True,
                          random_range_from=70,
                          random_range_to=140
                          )

# gizli hesaplardan falan uzak kalma muhabbeti
session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       skip_business=False,
                       skip_non_business=False,
                       )

# hangi tür hesapları muhattap alacağımız belirlemek
session.set_relationship_bounds(enabled=True,
				                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=1000000000,
                                min_followers=1000,
                                min_posts=10,
                                max_posts=100000000000)



def follow_(follow_tag_list = None, big_accounts = None):
	session.set_do_follow(enabled=True, percentage=50)
	# gizli hesaplardan falan uzak kalma muhabbeti
	session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       skip_business=False,
                       skip_non_business=False,
                       )

	if follow_tag_list is not None:
		foll_hash = session.target_list(follow_tag_list)
		session.follow_by_tags(foll_hash, amount=10)
		time.sleep(wait_time)

	if big_accounts is not None:
		big_accounts = session.target_list(big_accounts)
		# kullanıcını takipçilerinden takip et
		session.follow_user_followers(big_accounts, amount=100, randomize=True)
		time.sleep(wait_time)

		# takipçinin gönderilerini beğenenlerden takip et
		session.follow_likers(big_accounts, photos_grab_amount = 5, follow_likers_per_photo = 10, randomize=True, sleep_delay=600, interact=False)
		time.sleep(wait_time)
		# yorum atanları takip et
		session.follow_commenters(big_accounts, amount=100, daysold=365, max_pic = 60, sleep_delay=600, interact=False)
		time.sleep(wait_time)

    # unfollowing




def like_and_comment(like_tag_list, comments_list):

	# like jog
	session.set_do_like(enabled=True, percentage=70)
	session.set_do_comment(enabled=True, percentage=50)

	hashtags = session.target_list(like_tag_list)
	#comments = session.target_list(comments_list)

	session.set_delimit_liking(enabled=True, max_likes=10000000, min_likes=30)
	session.set_delimit_commenting(enabled=True, max_comments=None, min_comments=0)

	#session.like_by_tags(hashtags, amount=100)
	#time.sleep(wait_time)
		# comment job
	#session.set_comments(comments)
	session.set_comments(comments_list)
	time.sleep(wait_time)


	session.like_by_feed(amount=50, randomize=True, unfollow=True, interact=True)
	time.sleep(wait_time)




	# delimite yokken 3 beğenili fotoğrafları beğeniyor dolayısıyla onların bana bir yararı yok
	# az beğenili hesapları takipçilerin fazla görmeyi tercih etmediği hesaplardır diye tahmin ediyorum
    # gönderilerin altına yazılacak olan yorumları göster


def unfollowing():
	session.set_dont_unfollow_active_users(enabled=True, posts=5)
	session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
	time.sleep(wait_time)
