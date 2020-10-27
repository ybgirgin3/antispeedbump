# follow_tag_list: liste olmalı - main.py'dan gönderilecek
from instapy import InstaPy

# kullanıcı adı ve şifreyi gir sisteme
session = InstaPy(username='mental_huzur',
                  password='manzaralar1234', 
                  headless_browser=True
                  )
# giriş yap
session.login()



# durumları aktif et
session.set_do_follow(enabled=True, percentage=50)
# session.set_do_comment(enabled=True, percentage=50)
session.set_do_like(enabled=True, percentage=70)

# banlanmamak için supervisor aktif et
# limitler ile ilgili bilginin alındığı link: https://taplink.at/en/blog/instagram_follow_unfollow_limits_and_other_restrictions_2020.html#:~:text=In%202020%2C%20users%20are%20allowed,more%20freedom%20in%20this%20regard.
session.set_quota_supervisor(enabled=True,
                             sleep_after=["likes_h", "comments_h", "follows", "unfollows", "server_calls_h"],
                             sleepyhead=True, stochastic_flow=True, notify_me=True,
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

def follow_(follow_tag_list):
	# gönderilerin altındaki tagleri kullanan hesapları takip et
	session.set_dont_unfollow_active_users(enabled=True, posts=2)
	session.follow_by_tags(follow_tag_list)



def comment_(comments_list):
	# gönderilerin altına yazılacak olan yorumları göster
	#session.set_comments(comments_list)
	pass


def like_(like_tag_list):
	hashtags = session.target_list(like_tag_list)
	#session.set_smart_hashtags(like_tag_list, limit=5, sort='top', log_tags=True)
	#session.like_by_tags(amount=10, use_smart_hashtags=True)
	#session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)
	session.like_by_tags(hashtags, amount=10)




