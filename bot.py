import os
from typing import Optional

from commons import session
from utils import MediaProcess, Post, DBProcess
from commons.models.schemas import Sites


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

        # create session

    def get_data_from_another(self):
        with session() as sess:

            # create instance
            content = {}
            db_process = DBProcess(sess=sess, username=self.target_user)
            media_process = MediaProcess(username=self.target_user)

            def _fetch(u_w: str):
                content: dict = media_process.fetch()
                extracted_content: dict = media_process.parse(content=content)

                if self.will_create_content:
                    if u_w == 'write':
                        db_process.write(content, extracted_content)
                    if u_w == 'update':
                        db_process.update(content, extracted_content)

                return extracted_content

            # if file is not exists create
            is_exists = db_process.is_site_exists()
            if not is_exists:
                #content: dict = media_process.fetch()
                #extracted_content: dict = media_process.parse(content=content)
                extracted_content = _fetch(u_w='write')

            # if file exists
            else:
                # if look for date if valid
                if valid := db_process.is_site_still_valid(model=Sites):
                    print(
                        f"{self.target_user}'s file already exists. and valid. reading from cache")
                    extracted_content: dict = db_process.read(column='extracted_data')
                else:
                    extracted_content = _fetch(u_w='update')

            # extract content instance
            return extracted_content

    def post_content(self) -> None:
        def _post():
            # read flow file
            flow: list[dict] = DBProcess(filename='post', root="flow").read()

            # post content
            assert Post(post_information=flow[0]).post(
            ) == True, "post did not return True"

            # extract sent item and delete
            os.remove(flow.pop(0))

            # re-write item
            DBProcess(filename='post', root="flow", content=flow).write()

        def _story():
            flow: dict = DBProcess(filename='post', root="flow").read()
            print("flow file content in story: ", flow)

            assert Post(post_information=flow[0], device='mobile').story(
            ), "story did not return True"

            # extract sent item and delete
            os.remove(flow.pop(0))

        try:
            if self.post_type == "post":
                _post()
            elif self.post_type == "story":
                _story()

        except Exception as e:
            print("Error while post_content: ", e)
