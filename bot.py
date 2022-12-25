from utils import FileProcess, Process
from utils import Post
from typing import Optional


class Bot:
    def __init__(self,
                 target_user: Optional[str] = "",
                 will_create_content: Optional[bool] = False,
                 post_index: int = 0
                 ):
        self.target_user: str | None = target_user
        self.will_create_content = will_create_content
        self.post_index = post_index

    def get_data_from_another(self):
        # if file exists
        content: None = None
        is_site_exist: bool = FileProcess(
            filename=self.target_user).is_site_exists()
        if not is_site_exist:
            "if username is new create user data"
            resp: dict = Process(username=self.target_user).fetch()
            FileProcess(filename=self.target_user, content=resp).write()
        else:
            print(f"{self.target_user}'s file already exists. reading from cache")

        # extract content
        content = FileProcess(filename=self.target_user).read()
        extracted: dict = Process(content=content, post_index=self.post_index).parse()

        if self.will_create_content:
            created = Process(content=extracted).create_content()
            flow: list = FileProcess(filename='post', root="flow").read()
            if created not in flow:
                flow.append(created)
                flow = FileProcess(filename='post', root="flow",
                                   content=flow).write()
            else:
                print("content already in flow")

        return extracted

    def post_content(self):
        flow: list = FileProcess(filename='post', root="flow").read()

        Post(image=flow[0]).scenario()

        flow.pop(0)

        flow = FileProcess(filename='post', root="flow", content=flow).write()

        # return ret
