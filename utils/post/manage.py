# built-in
from typing import Optional, Union
import platform
from pathlib import Path

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
                 image: Optional[dict] = {}) -> None:
        self.url = url
        self.username = username
        self.passwd = passwd

        driver_path = os.path.join(Path().parent.absolute(
        ), f'configs/driver/{platform.system().lower()}/chromedriver')

        self.driver = set_driver(webdriver.Chrome(driver_path))
        self.get = get_driver()

    def process(self):
        "main process"
        go_to(self.url)  #  go to login

        # login
        # find buttons

        wait_until(Button("Log in").exists)  # wait for page fully loaded
        username_button = self._find_attr('@username', with_s=True)
        password_button = self._find_attr('@password', with_s=True)
        login_button = self._find_attr(Button("Log in"))

        # interact
        self._fill(username_button, self.username)
        self._fill(password_button, self.passwd)
        self._button_event(attr=login_button)

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

    # selenium way to solve
    # def _find_attr(self, select_by: str, attr: str, mapper: str):
    #     ret_attr = None
    #     if mapper.lower() == "selenium":
    #         method = getattr(By, select_by.upper())
    #         print("select element by: ", method)
    #         wait = WebDriverWait(webdriver, 5)
    #         ret_attr = webdriver.find_element(method, attr)
    #     else:
    #         sign = ""
    #         if select_by == 'name':
    #             sign = "@"

    #         ret_attr = find_all(S(f"{sign}{attr}"))

    #     return ret_attr
