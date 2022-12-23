from selenium import webdriver
from typing import Optional
from helium import *
import helium
import os


class Post:

    def __init__(self,
                 url: str = "www.instagram.com",
                 username: str = "kod_deneme",
                 passwd: str = "uZZc4-YBY:5sVW?",
                 image: Optional[dict] = {}) -> None:
        self.driver = set_driver(webdriver.Chrome('/Users/berkay/Documents/workspace/Data/antispeedbump/chromedriver'))

        self.url = url
        self.username = username
        self.passwd = passwd

    def process(self):
        "main process"
        get_driver()
        go_to(self.url)  # go to login

        # login
        self._fill(self.username, '@username')
        self._fill(self.passwd, "@password")
        self._button('press',  '//*[@id="loginForm"]/div/div[3]/button/div')



    def _fill(self, value: str, S: str = ""):
        """
            fill input fields with desired value

            @param: value: str
                         : value to fill

            @param: S    : str
                         : HTML attribute of field

        """
        attr = self._find_attr(S)
        if isinstance(attr, list):
            attr = attr[0]
        print("attr in _fill: ", attr)
        return write(value, into=attr)


    def _button(self, command: str, S: Optional[str] = ""):
        """
            @param: command : str
                            : click, press

            @param: value   : str
                            : Button Attr

            @param: S       : str [Optional]
                            : HTML attribute of button
                        

        """
        btn = self._find_attr(S)

        _command = getattr(helium, command)  # get function from helium
        _command(btn)
        # return _command(btn)

    def _find_attr(self, _S: str):
        if _S == "":
            pass
        ret = find_all(S(_S))
        if len(ret) > 1:
            print("Multiple Fields Found. Reconfigure your S -> ", _S)
        return ret[0]

