from utils import FileProcess, Process
from utils import Post
from typing import Optional



class Bot:
    def __init__(self,
                 target_user: Optional[str] = "",
                 image: Optional[dict] = {}
                 ):
        self.target_user = target_user
        self.image = image

    def get_data_from_another(self):
        # if file exists
        content = None
        is_site_exist = FileProcess(filename=self.target_user).is_site_exists()
        if not is_site_exist:
            "if username is new create user data"
            resp: dict = Process(username=self.target_user).fetch()
            FileProcess(filename=self.target_user, content=resp).write()

        # extract content
        content = FileProcess(filename=self.target_user).read()
        extracted = Process(content=content).parse()
        return extracted

    def post_content(self):
        ret = Post(image=self.image).process()
        return ret


# username = sys.argv[1]
# user_content = Bot(target_user=username).get_data_from_another()
# print(user_content)
# image = {
#     "path": "images/soldier.jpeg",
#     "description": "a cat which is ready to defend country"
#     }
# post_content = Bot(image=image).post_content()
# print("post_content: ", post_content)
