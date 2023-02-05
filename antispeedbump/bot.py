from typing import Optional

from antispeedbump.commons import session
from antispeedbump.commons.models.schemas import Sites, Queue
from antispeedbump.utils import MediaProcess, Post, DBProcess



class Bot:
    def __init__(
            self,
            target_user: Optional[str] = "",
            will_create_content: Optional[bool] = False,
            post_type: Optional[str] = "post",
    ):
        self.target_user = target_user
        self.will_create_content = will_create_content
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
                    if u_w == "write":
                        db_process.write(content, extracted_content)
                    if u_w == "update":
                        db_process.update(content, extracted_content)

                return extracted_content

            # if file is not exists create
            is_exists = db_process.is_site_exists()
            if not is_exists:
                if self.will_create_content:
                    print(f"{self.target_user}'s data couldn't found. creating..")
                extracted_content = _fetch(u_w="write")

            # if file exists
            else:
                # if look for date if valid
                if db_process.is_site_still_valid(model=Sites):
                    print(
                        f"{self.target_user}'s file already exists. and valid. reading from cache"
                    )
                    extracted_content: dict = db_process.read(
                        model=Sites,
                        column="extracted_data",
                        fetch_by=("username", self.target_user),
                    )
                else:
                    print(f"{self.target_user}'s file is older. Re-fetching..")
                    extracted_content: dict = _fetch(u_w="update")

            # extract content instance
            return extracted_content

    def post_content(self) -> None:
        def _post() -> None:
            """
            image post

            Return: None
            """
            with session() as sess:
                # create instance
                db_process = DBProcess(sess=sess, username=self.target_user)

                # read medias
                media: dict = db_process.read(model=Queue, column="medias")
                print("current media to upload: ",
                      media["id"], media["description"])

                # post content
                if Post(data_to_post=media).post() == True:
                    db_process.delete(Queue, media["id"])

        def _story():
            pass
            # flow: dict = DBProcess(filename="post", root="flow").read()
            # print("flow file content in story: ", flow)

            # assert Post(
            #    post_information=flow[0], device="mobile"
            # ).story(), "story did not return True"

            # extract sent item and delete
            # os.remove(flow.pop(0))

        # try:
        #    if self.post_type == "post":
        #        _post()
        #    elif self.post_type == "story":
        #        _story()

        # except Exception as e:
        #    print("Error while post_content: ", e)
        _post()
