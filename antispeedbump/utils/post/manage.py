# built-in
import os
import platform
from pathlib import Path
from typing import Union

import helium
from helium import *

# external
from selenium import webdriver

#  local
from .sub import _post, _story


class Post:
    def __init__(
        self,
        url: str = "www.instagram.com",
        # username: str = "koddeneme260",
        # passwd: str = "uZZc4-YBY:5sVW?",
        username: str = "bekocankod",
        passwd: str = ")d3::b%&.X,u3^J",
        data_to_post: dict = {},
    ) -> None:
        self.username = username
        self.passwd = passwd
        self.data_to_post = data_to_post
        self.url = url
        self.downloadable = self.download()

        #chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        firefox_options = webdriver.FirefoxOptions()

        # driver_path = os.path.join(
        #    Path().parent.absolute(),
        #    f"configs/driver/{platform.system().lower()}/chromedriver",
        # )

        driver_path = os.path.join(
            # Path().parent.absolute(),
            os.getcwd(),
            f"antispeedbump/configs/driver/{platform.system().lower()}/geckodriver"
        )

        #self._driver = webdriver.Chrome(driver_path, options=chrome_options)
        self._driver = webdriver.Firefox(
            executable_path=driver_path, options=firefox_options)
        self.driver = set_driver(self._driver)
        self.get = get_driver()

    def post(self) -> bool:
        return _post(self)

    def story(self) -> bool:
        return _story(self)

    def _fill(self, attr: str, value: str):
        """
        fill input fields with desired value

        @param: value: str
                     : value to fill

        @param: S    : str
                     : HTML attribute of field

        """
        return write(value, into=attr)

    def _button_event(self, command: str = "click", attr: Union[str, Button] = ""):
        """
        @param: command : str
                        : click, press

        @param: value   : str
                        : Button Attr

        @param: S       : str [Optional]
                        : HTML attribute of button


        """
        _command = getattr(helium, command)  # get function from helium
        print("_command from helium: ", _command)
        _command(attr)

    def _find_attr(self, attr, with_s: bool = False, prefix: str = None):
        print("attr in find_all: ", attr, type(attr))
        if with_s:
            attr = S(attr)

        ret = find_all(attr)
        print(prefix, ret)
        return ret

    def download(self) -> Union[dict, None]:

        media = self.data_to_post["media"]
        binary_data = self.data_to_post["binary_data"]
        is_video = media["is_video"]
        if is_video:
            filename = "blob.mp4"
        else:
            filename = "blob.jpeg"

        f = _download(blob=binary_data, filename=filename)

        return {
            "id": self.data_to_post['id'],
            "file_type": "video" if is_video else "image",
            "description": self.data_to_post["description"],
            "binary": f,
        }


def _download(blob, filename):
    import tempfile
    import os

    fp = os.path.join(tempfile.gettempdir(), filename)

    with open(fp, "wb") as f:
        f.write(blob)

    content_size = os.stat(fp).st_size
    if content_size <= 1024:
        print("content size is not bigger than 1024 mb")
        return None

    return fp


def delete(fp: str) -> None:
    import os

    """delete file from the os (not limited to project)

    Args:
        fp (str): _description_
    """
    os.remove(fp)
