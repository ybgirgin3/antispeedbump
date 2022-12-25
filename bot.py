from utils import FileProcess, Process
from utils import Post
from typing import Optional


class Bot:
    def __init__(self,
                 target_user: Optional[str] = "",
                 ):
        self.target_user: str | None = target_user

    def get_data_from_another(self):
        # if file exists
        content: None = None
        is_site_exist: bool = FileProcess(
            filename=self.target_user).is_site_exists()
        if not is_site_exist:
            "if username is new create user data"
            resp: dict = Process(username=self.target_user).fetch()
            FileProcess(filename=self.target_user, content=resp).write()

        # extract content
        content = FileProcess(filename=self.target_user).read()
        extracted: dict = Process(content=content).parse()
        return extracted

    def post_content(self):
        flow: list = FileProcess(filename='post', root="flow").read()

        Post(image=flow[0]).scenario()

        flow.pop(0)

        flow = FileProcess(filename='post', root="flow", content=flow).write()

        # return ret
