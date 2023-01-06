# built-in
from typing import Optional
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
    def __init__(self,
                 desktop_url: str = "www.instagram.com",
                 mobile_url: str = "i.instagram.com",
                 username: str = "koddeneme260",
                 passwd: str = "uZZc4-YBY:5sVW?",
                 # username: str = "bekocankod"
                 # passwd: str = ")d3::b%&.X,u3^J"
                 post_information: dict = None,
                 device: Optional[str] = 'desktop',

                 ) -> None:
        self.username = username
        self.passwd = passwd
        self.inf = post_information
        self.device = device
        self.url = mobile_url if self.device == "mobile" else desktop_url

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        if self.device == 'mobile':
            chrome_options.add_argument("--headless")
            chrome_options.add_experimental_option(
                "mobileEmulation", {
                    "deviceMetrics": {
                        "width": 390,
                        "height": 844,
                        "mobile": True,
                        "deviceScaleFactor": 0
                    },
                    # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
                })

        driver_path = os.path.join(Path().parent.absolute(
        ), f'configs/driver/{platform.system().lower()}/chromedriver')

        self._driver = webdriver.Chrome(
            driver_path, options=chrome_options)

        self.driver = set_driver(self._driver)
        self.get = get_driver()

    def post(self) -> bool:
        print("api url: ", self.url)
        try:
            # *** LOGIN
            self.login()

            # *** share
            share_button = self._find_attr(
                "//*[name()='svg' and @aria-label='New post']", with_s=True)[0]
            # find button
            wait_until(share_button.exists)
            self._button_event(attr=share_button)

            # attach file
            drag_file(self.inf['path'],
                      to="Drag photos and videos here")

            # is_video?
            if self.inf['is_video']:
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
                attr="//*[name()='textarea' and @aria-label='Write a caption...']",
                with_s=True)[0]
            wait_until(desc_area.exists)
            self._fill(attr=desc_area,
                       value=self.inf['description'] if 'description' in
                       self.inf else "")

            # Share post
            sb = Button("Share")
            wait_until(sb.exists)
            self._button_event(attr=sb)

            return True

        except Exception as e:
            print("Error while posting content: ", e)
            return False

    """
   
    def upload_story_photo(self, photo, upload_id=None):
        if upload_id is None:
            upload_id = str(int(time.time() * 1000))
        photo = stories_shaper(photo)
        if not photo:
            return False

        with open(photo, "rb") as f:
            photo_bytes = f.read()

        data = {
            "upload_id": upload_id,
            "_uuid": self.uuid,
            "_csrftoken": self.token,
            "image_compression": '{"lib_name":"jt","lib_version":"1.3.0",'
            + 'quality":"87"}',
            "photo": (
                "pending_media_%s.jpg" % upload_id,
                photo_bytes,
                "application/octet-stream",
                {"Content-Transfer-Encoding": "binary"},
            ),
        }
        m = MultipartEncoder(data, boundary=self.uuid)
        self.session.headers.update(
            {
                "Accept-Encoding": "gzip, deflate",
                "Content-type": m.content_type,
                "Connection": "close",
                "User-Agent": self.user_agent,
            }
        )
        response = self.session.post(config.API_URL + "upload/photo/", data=m.to_string())

        if response.status_code == 200:
            upload_id = json.loads(response.text).get("upload_id")
            if self.configure_story(upload_id, photo):
                # self.expose()
                return True
        return False
    
    """

    def story(self) -> bool:

        pass

    def _story(self) -> bool:
        print("api url: ", self.url)
        # *** LOGIN
        self.login()

        # *** SHARE

        # new post button
        post_button = self._find_attr(
            "//*[name()='svg' and @aria-label='Home']", with_s=True)[0]
        wait_until(post_button.exists)
        self._button_event(attr=post_button)

        # story button
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
        inp_field.send_keys(self.inf['path'])

        # attach_file(file_path=self.inf['path'])

        return False

    def login(self):
        go_to(self.url)  # go to url
        if self.device == "desktop":
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

        elif self.device == "mobile":
            # find log in button
            pre_login = Button("Log in")
            wait_until(pre_login.exists)
            pre_login_button = self._find_attr(pre_login)[0]
            self._button_event(attr=pre_login_button)

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

            # *** Add to Home Screen ??
            c = Button("Cancel")
            wait_until(c.exists)
            # find button
            cancel_button = self._find_attr(c)[0]
            self._button_event(attr=cancel_button)

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

    # util
    def _post_resp(self):
        resp: Response
