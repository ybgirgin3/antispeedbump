# follow_tag_list: liste olmalı - main.py'dan gönderilecek
from instapy import InstaPy
from inf import USERNAME, PASSWORD


# kullanıcı adı ve şifreyi gir sisteme
session = InstaPy(username=USERNAME,
                  password=PASSWORD, 
                  headless_browser=True,
                  disable_image_load=True,
                  )
# giriş yap
session.login()



# durumları aktif et

# banlanmamak için supervisor aktif et
# limitler ile ilgili bilginin alındığı link: https://taplink.at/en/blog/instagram_follow_unfollow_limits_and_other_restrictions_2020.html#:~:text=In%202020%2C%20users%20are%20allowed,more%20freedom%20in%20this%20regard.
session.set_quota_supervisor(enabled=True,
                             sleep_after=["likes_d", "follows_d"],
                             sleepyhead=True, 
                             stochastic_flow=True, 
                             notify_me=True,
                             peak_likes_hourly=41,
                             peak_likes_daily=500,
                             peak_comments_hourly=21,
                             peak_comments_daily=182,
                             peak_follows_hourly=20,
                             peak_follows_daily=200,
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=200,
                             peak_server_calls_hourly=None,
                             peak_server_calls_daily=4700)

session.set_action_delays(enabled=True,
                          like=3,
                          comment=5,
                          follow=4.17,
                          unfollow=28,
                          story=10)

session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       skip_business=False,
                       skip_non_business=False,
                       )


session.set_relationship_bounds(enabled=True,
				                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=1000000000,
                                min_followers=1000,
                                min_posts=10,
                                max_posts=100000000000)



def follow_(follow_tag_list, big_accounts = None):
    session.set_do_follow(enabled=True, percentage=50)
    foll_hash = session.target_list(follow_tag_list)
    session.follow_by_tags(foll_hash, amount=10)

    if big_account:
        big_accounts = session.target_list(big_accounts)
		# kullanıcını takipçilerinden takip et
        session.follow_user_followers(big_accounts, amount=100, randomize=True)
		# takipçinin gönderilerini beğenenlerden takip et
        session.follow_likers(big_accounts, photos_grab_amount = 5, follow_likers_per_photo = 10, randomize=True, sleep_delay=600, interact=False)
		# yorum atanları takip et
        session.follow_commenters(big_accounts, amount=100, daysold=365, max_pic = 60, sleep_delay=600, interact=False)


def like_(like_tag_list):
	
	"""
	like için bir liste zaten lazımdı
	"""
	session.set_do_like(enabled=True, percentage=70)
	hashtags = session.target_list(like_tag_list)

	# delimite yokken 3 beğenili fotoğrafları beğeniyor dolayısıyla onların bana bir yararı yok
	session.set_delimit_liking(enabled=True, max_likes=10000000, min_likes=2000)
	session.like_by_tags(hashtags, amount=100)



def comment_(comments_list):
    # session.set_do_comment(enabled=True, percentage=50)
	# gönderilerin altına yazılacak olan yorumları göster
	#session.set_comments(comments_list)
	pass

