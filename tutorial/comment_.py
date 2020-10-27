from instapy import InstaPy

session = InstaPy(username='mental_huzur',
                  password='manzaralar1234', 
                  headless_browser=True
                  )
session.login()

session.set_do_comment(enabled=True, percentage=25)
session.set_comments(['Beautiful', 'Nice', 'Awesome'])

session.interact_by_URL(urls=["https://www.instagram.com/p/CG0ovz-sf_M/?utm_source=ig_web_copy_link"],
                        randomize=True,
                        interact=True)
