# link: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
from instapy import InstaPy

session = InstaPy(username='mental_huzur',
                  password='manzaralar1234', 
                  headless_browser=True
                  )
session.login()
session.set_action_delays(enabled=True,
                          like=3,
                          comment=5,
                          follow=4.17,
                          unfollow=28,
                          story=10)



# 
#session.set_do_like(enable=True, percentage=70)

# burda verilen taglere göre fotoğraf beğenecek
session.like_by_tags(['huzur', 'psikoloji', 'hayat', 'cennet'], amount=10)

# etkileşime geçilecek hesapları
session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100,
                       skip_business=False,
                       skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[],
                       skip_bio_keyword=[],
                       mandatory_bio_keywords=[])

# en son 5 postumu beğenen kullanıcıları takipten çıkarma
# şimdilik 2 
session.set_dont_unfollow_active_users(enabled=True, posts=2)

# bu min ve max arasındaki beğenilere sahip olan sayfaları beğen
session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)


# burdaki taglere göre beğenileri beğenmeyecek
#session.set_dont_like(['naked', 'nsfw'])

# fotoğrafını beğendiği elemanları takip edecek
session.set_do_follow(True, percentage=50, times=2)
session.follow_by_tags(['huzur', 'mutluluk', 'cennet', 'peygamber'], amount=10)


# yorum yapacak
session.set_do_comment(True, percentage = 50)
session.set_comments(["nice, sweet, beautiful :heart_eyes:"])

session.set_action_delays(enabled=True,
                          like=3,
                          comment=5,
                          follow=4.17,
                          unfollow=28,
                          story=10)

# instagram eğer bot olduğunuzu anlarsa direk olarak banlar o yüzden yasal sınırlar içerisinde bu işi yap
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

# çok fazla takipçisi olan sayfalar takip etmek anlamsız geri dönüş olmaz falan 
# ama gönderilerine yorum yapmak mantıklı olabilir.
session.set_relationship_bounds(enabled=True, max_followers=8500)







