import time
import random

wt = random.randint(90, 300)

def unfollow(session):
    session.set_dont_follow_active_users(enabled=False, posts = 10)
    time.sleep(wt)
