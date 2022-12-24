# built-in
from typing import Optional
import platform
from pathlib import Path

import os

# external
from selenium.webdriver.common.by import By
from selenium import webdriver
from helium import *
import helium


class Post:

    def __init__(self,
                 url: str = "www.instagram.com",
                 username: str = "koddeneme260",
                 passwd: str = "uZZc4-YBY:5sVW?",
                 # username: str = "bekocankod"
                 # passwd: str = ")d3::b%&.X,u3^J"
                 image: Optional[dict] = {}) -> None:
        driver_path = os.path.join(Path().parent.absolute(
        ), f'configs/driver/{platform.system().lower()}/chromedriver')
        self.driver = set_driver(webdriver.Chrome(driver_path))
        self.get = get_driver()

        self.url = url
        self.username = username
        self.passwd = passwd

    def process(self):
        "main process"
        go_to(self.url)  #  go to login

        # login
        self._fill(self.username, '@username')
        self._fill(self.passwd, "@password")
        self._button(
            'press', '//*[@id="loginForm"]/div/div[3]/button', custom_attr=False)

    def _fill(self, value: str, S: str = ""):
        """
            fill input fields with desired value

            @param: value: str
                         : value to fill

            @param: S    : str
                         : HTML attribute of field

        """
        attr = self._find_attr(S)
        print("attr in _fill: ", type(attr))
        print("attr in _fill: ", attr)
        return write(value, into=attr)

    def _button(self, command: str, S: Optional[str] = "", custom_attr=False):
        """
            @param: command : str
                            : click, press

            @param: value   : str
                            : Button Attr

            @param: S       : str [Optional]
                            : HTML attribute of button


        """
        if custom_attr:
            btn = self._find_attr(S)[0]
        else:
            btn = S

        _command = getattr(helium, command)  # get function from helium
        _command(btn)
        # return _command(btn)

    def _find_attr(self, _S: str):
        if _S != "":
            return find_all(S(_S))

    # selenium way to solve
    # def _find_attr(self, _S: str):
    #     if _S != "":
    #         p = None
    #         if _S.startswith('/') or _S.startswith("//"): # xpath
    #             p = _S
    #             _S = By.XPATH

    #         if _S.startswith("@"): # name
    #             p = _S[1:]
    #             _S = By.NAME

    #         # ret = find_all(S(_S))
    #         ret = self.get.find_element(_S, p)
    #         return ret
