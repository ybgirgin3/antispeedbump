from utils import FileProcess, Process
from utils import Post
from typing import Optional


class Bot:
    def __init__(self,
                 target_user: Optional[str] = "",
                 will_create_content: Optional[bool] = False
                 ):
        self.target_user: str | None = target_user
        self.will_create_content = will_create_content

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

        if self.will_create_content:
            print(":Content Creating:")
            created = Process(content=extracted).create_content()
            print(":Content Created:")
            print(":Content Adding to flow.json:")
            flow: list = FileProcess(filename='post', root="flow").read()
            print("old flow: ", flow)
            flow.append(created)
            print("new flow: ", flow)
            flow = FileProcess(filename='post', root="flow",
                               content=flow).write()

        return extracted

    def post_content(self):
        flow: list = FileProcess(filename='post', root="flow").read()

        Post(image=flow[0]).scenario()

        flow.pop(0)

        flow = FileProcess(filename='post', root="flow", content=flow).write()

        # return ret
