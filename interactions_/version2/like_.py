import time
import random

wt = random.randint(90, 300)

def like(session, like_tag_list = None):
    # eğer fonksiyona bir liste gönderilmezse
    # feed üzerindeki gönderileri beğenemeye başlayacak
    session.set_delimit_liking(enable=True, max_likes = 10000000, min_likes = 6)

    if like_tag_list is None:
        session.like_by_feed(amount=50, randomize=True, unfollow=True, interact = True)
        print(f'{wt} SN BEKLEME SÜRESİ BAŞLADI')
        time.sleep(wt)

    elif like_by_feed is not None:
        tags = session.target_list(like_tag_list)
        session.like_by_tags(tags, amount=100)
        print(f'{wt} SN BEKLEME SÜRESİ BAŞLADI')
        time.sleep(wt)




