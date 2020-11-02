
def comment(session, comment_list = None):
    # comment list vermişken onlara göre yorum yapacak
    # yokken kendine göre yorum yapacak

    # listelediğim yorumlar bir işe yaramıyor ama denemekte fayda var

    # kısıtlama olan satır aslında bir işe yaramayacak çünkü zaten min ve max commentlere gerek yok
    #session.set_delimit_commenting(enable = True, max_comments = None, min_comments = 0)

    if comment_list is not None:
        comm = session.target_list(comment_list)
        session.set_comments(comm)

    elif comment_list is None:
        print('comment list bulunamadı.. umarım varsayılan yorumlardan kullanır ldjfshldf')
        pass


