from instapy import InstaPy
from inf import USERNAME, PASSWORD

session = InstaPy(username=USERNAME, password = PASSWORD, headless_browser = True, geckodriver_path='/home/berkay/InstaPy/assets/gecko/v0.27.0/geckodriver-v0.27.0-linux64/geckodriver')
session.login()


session.set_quota_supervisor(enabled=True,
        sleep_after=["likes", "comments_d", "follows_h", "unfollows_h", "server_calls_h"],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes_hourly=30,
        peak_likes_daily=200,
        peak_comments_daily=21,
        peak_follows_daily=100,
        peak_unfollows_daily=10,
        peak_server_calls_hourly=500,
        peak_server_calls_daily=600)


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


session.set_skip_users(skip_private=True,
        private_percentage=100,
        skip_no_profile_pic=True,
        skip_business=False,
        skip_non_business=False,
        )


def job(big_accounts=None, comments_list=None):
    
	# set delimitings
	session.set_delimit_liking(enabled=True, max_likes=10000000, min_likes=30)
	session.set_delimit_commenting(enabled=True, max_comments=None, min_comments=100)


	# set like type
	session.like_by_feed(amount=50, randomize=True, unfollow=True, interact=True)
    session.like_by_tag(like_tags, amount=1000)

	#set comments and type
	comments_list = session.target_list(comments_list)
	session.set_comments(comments_list)

	# enable actions
	session.set_do_follow(enabled=False, percentage=50)
	session.set_do_like(enabled=True, percentage=50)
	session.set_do_comment(enabled=True, percentage=50)


def unf():
    session.set_dont_unfollow_activate_users(enabled=True, posts=10)
    session.unfollow_users(amount=120, nonFollowers=True, style, unfollow_after=24*6*60, sleep_delay=655))

