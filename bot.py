from utils import FileProcess, Process
from typing import Optional
import sys

username = sys.argv[1]


class Bot:
    def __init__(self, target_user: Optional[str] = None):
        self.target_user = target_user

    def get_data_from_another(self):
        # if file exists
        content = None
        is_site_exist = FileProcess(filename=username).is_site_exists()
        if not is_site_exist:
            "if username is new create user data"
            print("data not exists")
            resp: dict = Process(username=username).fetch()
            FileProcess(filename=username, content=resp).write()

        # extract content
        content = FileProcess(filename=username).read()
        extracted = Process(content=content).parse()
        return extracted

    def post_content(self):
        pass


user_content = Bot(target_user=username).get_data_from_another()
print("user_content: ", user_content)
