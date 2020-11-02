import time
import random

wt = random.randint(90, 300)

def follow(
        session,
        big_accounts = None,
        follow_tag_list = None):

    # adı verilmiş olan büyük hesapların takipçilerini takip et
    if big_accounts is None:
        print('big account listesi bulunamadı pas geçiliyor')
        pass

    else:
        bigacc = session.target_list(big_accounts)
        session.follow_user_followers(bigacc, amount=100, randomize=True)
        print(f'{wt} SN BEKLEME SÜRESİ BAŞLADI')
        time.sleep(wt)

    # verilen listedeki tagleri postlarında kullanan kullanıcıları takip et
    if follow_tag_list is None:
        print('follow_tag_list bulunamadı pas geçiliyor')
        pass

    else:
        follow_tag = session.target_list(follow_tag_list)
        session.follow_by_tags(follow_tag, amount = 10)
        print(f'{wt} SN BEKLEME SÜRESİ BAŞLADI')
        time.sleep(wt)




