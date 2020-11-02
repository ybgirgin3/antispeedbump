# follow, unfollow, like, comment işlemlerinin hepsi tek tek modüller olarak çağrılacak
import os
import sys
import time
from instapy import InstaPy
from instapy import smart_run


# kendi modüllerim
from inf import username, password
from follow_ import follow
from unfollow_ import unfollow
from like_ import like
from comment_ import comment


# dosya yolları 
follow_tags = 'follow_tag_file.txt'
like_tags = 'like_tag_file.txt'
comments = 'comments.txt'
target_accounts = 'big_accounts.txt'

# tanımlamalar ve kısıtlamalar
session = InstaPy(
        username = username,
        password = password,
        headless_browser = True
        )

# kotalar
session.set_quota_supervisor(
        enabled = True,
        sleep_after = ["likes", "comments_h", "follows_h", "unfollows_h", "server_calls_h"],
        sleepyhead = True,
        stochastic_flow = False,
        notify_me = True,
        peak_likes_hourly = 20,
        peak_likes_daily = 500,
        peak_comments_hourly = 21,
        peak_comments_daily = 100,
        peak_follows_hourly = 35,
        peak_follows_daily = 100,
        peak_unfollows_hourly = 35,
        peak_unfollows_daily = 100,
        peak_server_calls_hourly = 200,
        peak_server_calls_daily=3700)

# işlemlerden sonra bekleme
session.set_action_delays(
        enabled = True,
        like = 30,
        comment = 30,
        follow = 71,
        unfollow = 28,
        story = 10,
        randomize = True,
        random_range_from = 70,
        random_range_to = 140)

# pas geçilecek olan hesaplar
session.set_skip_users(
        skip_private = False,
        private_percentage = 25,
        skip_no_profile_pic = False,
        skip_business = False,
        skip_non_business = False)

# muhatap alınacak olan hesaplar
session.set_relationship_bounds(
        enabled = True,
        delimit_by_numbers = True,
        min_followers = 60,
        min_posts = 0)


# işlemleri aktive et

with smart_run(session, threaded=True):
    # önce fonksiyonları çağırmak lazım
    # follow
    follow(
        session,
        big_accounts = target_accounts,
        follow_tag_list = follow_tags)
    
    # like
    like(session, like_tag_list= like_tags)

    # comments
    comment(session, comment_list=comments)

    # unfollow
    unfollow(session)

    
    
    
    # işlemleri en son tanımlamak gerekiyor
    session.set_do_follow(enabled=True, percentage=50)
    session.set_do_like(enabled=True, percentage=50)
    session.set_do_comment(enabled=True, percentage=50)

    # bot sürekli çalışır hale geldikten sonra aşağıdaki unfollow satırına
    # unfollow_after = 48*60*60
    # komutunu da eklemek gerekli
    session.set_do_unfollow_users(enabled=True, nonFollowers=True, style="LIFO", sleep_delay=655)
    pass


