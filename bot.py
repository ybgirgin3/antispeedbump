from utils import FileProcess, Process, Post, _delete
from typing import Optional


class Bot:
    def __init__(self,
                 target_user: Optional[str] = "",
                 will_create_content: Optional[bool] = False,
                 post_index: Optional[int] = 0,
                 shortcode: Optional[str] = "",
                 post_type: Optional[str] = "post"
                 ):
        self.target_user = target_user
        self.will_create_content = will_create_content
        self.post_index = post_index
        self.shortcode = shortcode
        self.post_type = post_type

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
        extracted: dict = Process(
            content=content, post_index=self.post_index).parse()

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
        def _post():
            # read flow file
            flow: list = FileProcess(filename='post', root="flow").read()

            # post content
            assert Post(post_information=flow[0]).post(
            ) == True, "post did not return True"

            # extract sent item and delete
            _delete(flow.pop(0))

            # re-write item
            flow = FileProcess(
                filename='post', root="flow", content=flow).write()

        def _story():
            flow: list = FileProcess(filename='post', root="flow").read()
            assert Post(post_information=flow[0], device='mobile').story(
            ) == True, "story did not return True"

            # extract sent item and delete
            # _delete(flow.pop(0))

        try:
            if self.post_type == "post":
                _post()
            elif self.post_type == "story":
                _story()

        except Exception as e:
            print("Error while post_content: ", e)
