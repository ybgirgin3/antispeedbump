# kütüphaneler çağırmaya gerek yok

# follow_tag_list: liste olmalı - main.py'dan gönderilecek

# durumları aktif et
session.set_do_follow(enabled=True, percentage=50)
session.set_do_comments(enabled=True, percentage=50)
session.set_do_like(enabled=True, percentage=70)

def follow_(follow_tag_list):
	# gönderilerin altındaki tagleri kullanan hesapları takip et
	session.follow_by_tags(follow_tag_list)


def comment_(comments_list):
	# gönderilerin altına yazılacak olan yorumları göster
	session.set_comments(comments_list)


def like_(like_tag_list):
	session.set_smart_hashtags(like_tag_list, limit=5, sort='random', log_tags=True)
	session.like_by_tags(amount=10, use_smart_hashtags=True)



