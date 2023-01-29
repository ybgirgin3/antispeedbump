# built-in
from typing import Optional, Union
from pathlib import Path
from requests import Response
import platform
import requests
import time
import os

# external
from selenium.webdriver.common.by import By
from selenium import webdriver
from helium import *

import selenium
import helium


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

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        driver_path = os.path.join(
            Path().parent.absolute(),
            f"configs/driver/{platform.system().lower()}/chromedriver",
        )

        self._driver = webdriver.Chrome(driver_path, options=chrome_options)
        self.driver = set_driver(self._driver)
        self.get = get_driver()

    def post(self) -> bool:
        print("api url: ", self.url)
        try:
            # *** LOGIN
            self.login()

            # *** share
            share_button = self._find_attr(
                "//*[name()='svg' and @aria-label='New post']", with_s=True
            )[0]
            # find button
            wait_until(share_button.exists)
            self._button_event(attr=share_button)

            # attach file
            drag_file(self.downloadable["binary"], to="Drag photos and videos here")

            # is_video?
            if self.downloadable["file_type"] == "video":
                ok = Button("OK")
                wait_until(ok.exists)
                self._button_event(attr=ok)

            # *** Aspect Ration
            # crop button
            crop_button = self._find_attr(
                "//*[name()='svg' and @aria-label='Select crop']", with_s=True
            )[0]
            wait_until(crop_button.exists)
            self._button_event(attr=crop_button)

            # original button
            org = Button("Original")
            wait_until(org.exists)
            self._button_event(attr=org)

            # next session (two times in a row)
            # first
            ns = Button("Next")
            wait_until(ns.exists)
            self._button_event(attr=ns)

            time.sleep(3)

            # second
            ns = Button("Next")
            wait_until(ns.exists)
            self._button_event(attr=ns)

            # *** Write a Description
            # find description area
            time.sleep(3)
            desc_area = self._find_attr(
                attr="//*[name()='textarea' and @aria-label='Write a caption...']",
                with_s=True,
            )[0]
            wait_until(desc_area.exists)
            # NOTE:EMOJI TO UNICODE VALIDATION YAZ
            self._fill(
                attr=desc_area,
                value=self.downloadable["description"],
            )

            # Share post
            sb = Button("Share")
            wait_until(sb.exists)
            self._button_event(attr=sb)

            return True

        except Exception as e:
            print("Error while posting content: ", e)
            return False

    def story(self) -> bool:
        return False

    def _story(self) -> bool:
        print("api url: ", self.url)
        # *** LOGIN
        self.login()

        # *** SHARE

        # new post button
        post_button = self._find_attr(
            "//*[name()='svg' and @aria-label='Home']", with_s=True
        )[0]
        wait_until(post_button.exists)
        self._button_event(attr=post_button)

        # story button
        sb = "//*[name()='svg' and @aria-label='Story']"
        story_button = self._find_attr(sb, with_s=True)[0]
        wait_until(story_button.exists)
        self._button_event(attr=story_button)

        # input for story
        inp = "//input[@type='file']"
        # inp_field = self._find_attr(inp, with_s=True)[0]
        # wait_until(inp_field.exists)
        # self._button_event(attr=)

        inp_field = self._driver.find_element(By.XPATH, inp)
        inp_field.send_keys(self.inf["path"])

        # attach_file(file_path=self.inf['path'])

        return False

    def login(self):
        go_to(self.url)  # go to url
        # ***  LOGIN
        wait_until(Button("Log in").exists)  # wait for page fully loaded

        # find buttons
        username_button = self._find_attr("@username", with_s=True)[0]
        password_button = self._find_attr("@password", with_s=True)[0]
        login_button = self._find_attr(Button("Log in"))[0]

        #  interact
        self._fill(username_button, self.username)
        self._fill(password_button, self.passwd)
        self._button_event(attr=login_button)

        # *** Save Your Login Info?
        nn = Button("Not Now")
        wait_until(nn.exists)
        # find button
        not_now_button = self._find_attr(nn)[0]
        self._button_event(attr=not_now_button)

        # *** Turn on Notifications?
        nn = Button("Not Now")
        wait_until(nn.exists)
        # find button
        not_now_button = self._find_attr(nn)[0]
        self._button_event(attr=not_now_button)

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

    def _find_attr(self, attr, with_s: bool = False):
        print("attr in find_all: ", attr, type(attr))
        if with_s:
            attr = S(attr)

        ret = find_all(attr)
        print("ret: ", ret)
        return ret

    def download(self) -> dict:
        import uuid

        media = self.data_to_post["media"]
        is_video = media["is_video"]
        media_url = media["download_url"]
        if is_video:
            filename = f"{uuid.uuid4()}.mp4"
        else:
            filename = f"{uuid.uuid4()}.jpeg"

        return {
            "file_type": "video" if is_video else "image",
            "description": self.data_to_post["description"] + "\u2764",
            "binary": _download(url=media_url, filename=filename),
        }


def _download(url: str, filename: str) -> str:
    import requests
    import tempfile
    import uuid
    import os

    fp = os.path.join(tempfile.gettempdir(), filename)

    resp = requests.get(url)  # making requests to server

    with open(fp, "wb") as f:  # opening a file handler to create new file
        f.write(resp.content)

    return fp


def delete(fp: str) -> None:
    import os

    """delete file from the os (not limited to project)

    Args:
        fp (str): _description_
    """
    os.remove(fp)
