# built-in
from zipfile import ZipFile
from tqdm import tqdm
import requests
import os
import sys
import platform
from typing import Union, Optional
from pathlib import Path

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
            username: str = "",
            password: str = "",
            # username: str = "koddeneme260",
            # passwd: str = "uZZc4-YBY:5sVW?",
            # username: str = "bekocankod",
            # passwd: str = ")d3::b%&.X,u3^J",
            data_to_post: dict = {},
            driver_path: Optional[str] = os.path.join(
                os.getcwd(),
                f"antispeedbump/configs/driver/{platform.system().lower()}/chromedriver"
            )
    ) -> None:
        self.username = username
        self.passwd = password
        self.data_to_post = data_to_post
        self.url = url
        self.downloadable = self.download()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")

        if not Path(driver_path).is_file():  # if driver is in path
            download_driver()

        self._driver = webdriver.Chrome(driver_path, options=chrome_options)

        version_control(self._driver)

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


def download_driver(chunk_size=128):
    new_ver = str(input("Newer version of chromedriver [ref: https://chromedriver.storage.googleapis.com/index.html] :"))

    o = {
            "darwin": "mac",
            "linux": "linux",
            "windows": "windows"
            }
    v = {
            "arm64": "arm64",
            "x86_64": "{}64",
        }

    _os = f"{o[platform.system().lower()]}_{v[os.uname().machine]}"

    _fn = f"chromedriver_{_os}.zip"
    _path = f"antispeedbump/configs/driver/{platform.system().lower()}"
    fn = f"{_path}/{_fn}"
    url = f"https://chromedriver.storage.googleapis.com/{new_ver}/{_fn}"
    r = requests.get(url, stream=True)
    total = int(r.headers.get('content-length', 0))

    # download zip file
    pbar = tqdm(total=total, unit="iB", unit_scale=True, unit_divisor=1024) 
    with open(fn, 'wb') as f:
        pbar.set_description(f"Downloading driver {fn}")
        for chunk in r.iter_content(chunk_size=chunk_size):
            s = f.write(chunk)
            pbar.update(s)

    # unzip file
    with ZipFile(fn, 'r') as zObj:
        zObj.extractall(_path)
        print("file extracted")

    # make file executable
    os.system(f"chmod +x {_path}/chromedriver")


    sys.exit(1)


def version_control(driver):
    """control version of chrome and match it to chromedriver"""

    br_ver = driver.capabilities['browserVersion']
    ch_ver = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

    print("version of browserVersion: ", br_ver)
    print("version of chromedriverversion: ", ch_ver)

    #ver.split(".")[0]
    if int(br_ver.split(".")[0]) != int(ch_ver.split(".")[0]):
        new_dr_perm = str(input("Different version of driver needs to be installed. Do you want to continue: [Y/n]" ))
        if new_dr_perm in ('Y', 'y'):
            if download_driver():
                print("please re-start app..")
                sys.exit(1)
            else:
                print("unknown error while installing driver..")
        else: 
            print("unable to continue with unmatched version of driver.. exiting...")

