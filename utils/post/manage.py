# built-in
from typing import Optional
from pathlib import Path
import platform
import time
import os

# external
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from helium import *

import selenium
import helium


class Post:

    def __init__(self,
                 url: str = "www.instagram.com",
                 username: str = "koddeneme260",
                 passwd: str = "uZZc4-YBY:5sVW?",
                 # username: str = "bekocankod"
                 # passwd: str = ")d3::b%&.X,u3^J"
                 image: dict = None) -> None:
        self.url = url
        self.username = username
        self.passwd = passwd
        self.posting_content = image

        driver_path = os.path.join(Path().parent.absolute(
        ), f'configs/driver/{platform.system().lower()}/chromedriver')

        self.driver = set_driver(webdriver.Chrome(driver_path))
        self.get = get_driver()

    def scenario(self):
        "main process"
        go_to(self.url)  #  go to login

        # ***  LOGIN 
        wait_until(Button("Log in").exists)  # wait for page fully loaded
        # find buttons

        username_button = self._find_attr('@username', with_s=True)[0]
        password_button = self._find_attr('@password', with_s=True)[0]
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

        # *** share
        share_button = self._find_attr(
            "//*[name()='svg' and @aria-label='New post']", with_s=True)[0]
        # find button
        wait_until(share_button.exists)
        self._button_event(attr=share_button)

        # attach file
        drag_file(self.posting_content['path'],
                  to="Drag photos and videos here")

        # is_video?
        if self.posting_content['is_video']:
            ok = Button("OK")
            wait_until(ok.exists)
            self._button_event(attr=ok)

        # *** Aspect Ration 
        # crop button
        crop_button = self._find_attr(
            "//*[name()='svg' and @aria-label='Select crop']", with_s=True)[0]
        wait_until(crop_button.exists)
        self._button_event(attr=crop_button)

        # original button
        org = Button("Original")
        wait_until(org.exists)
        self._button_event(attr=org)

        # next session (two times in a row)
        # first
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
            attr="//*[name()='textarea' and @aria-label='Write a caption...']", with_s=True)[0]
        wait_until(desc_area.exists)
        self._fill(attr=desc_area,
                   value=self.posting_content['description'] if 'description' in self.posting_content else "")

        # Share post
        sb = Button("Share")
        wait_until(sb.exists)
        self._button_event(attr=sb)

        # Your post has been shared?
        # time.sleep(3)
        # t = Text("Your post has been shared.")
        # wait_until(sb.exists)
        # if self._find_attr(t.exists):
        #     print("Post Sharing Successfull")

    def _fill(self, attr: str, value: str):
        """
            fill input fields with desired value

            @param: value: str
                         : value to fill

            @param: S    : str
                         : HTML attribute of field

        """
        return write(value, into=attr)

    def _button_event(self, command: str = "click", attr: str = ""):
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
