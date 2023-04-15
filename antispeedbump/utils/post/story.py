from utils import complete_dict
import datetime
import requests
import time
import json

# for type
from requests import Response

# upload_id = str(int(time.time() * 1000))


def _(fn):
  with open(f"configs/settings/post/{fn}") as f:
    return json.load(f)


GET_HEADERS = _("story.json")


class Story:
  story_headers = {
    "referrer": "https://www.instagram.com/create/story/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    f"body": "upload_id={_upload_id}&caption=",
    # "method": "POST",
    # "mode": "cors",
    # "credentials": "include"
  }
  login_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": "{csrftoken}",
  }
  username = "SessionDeneme"
  password = "'G7&z-E/*Gx4k^"

  payload = {
    "username": username,
    # "password": password,
    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{_time}:{password}",
  }

  def __init__(self) -> None:
    self.story_url = (
      "https://www.instagram.com/api/v1/web/create/configure_to_story/"
    )
    self.login_url = "https://www.instagram.com/api/v1/web/data/shared_data/"

    self.upload_id = str(int(time.time() * 1000))
    self.story_headers = complete_dict(
      raw_headers=GET_HEADERS, custom_headers=self.story_headers
    )

    self.session = requests.Session()

    # TODO:
    # * Resmin boyutları story boyutlarına uyuyor mu onu kontrol et.
    # * uyuyorsa eğer binary olarak kayıt işlemlerini yeniden yap
    # * csrf tokenları vs alma işlemine devam et

    def _login(self):
      _time: int = int(datetime.datetime.timestamp())

      # get login tokens
      response = requests.get(self.login_url)
      csrf = response.cookies["csrftoken"]

      self.login_headers.format(csrftoken=csrf)


# class Story:
#    # url = 'https://www.instagram.com/accounts/login/'
#    url = "https://www.instagram.com/api/v1/web/data/shared_data/"
#    # login_url = 'https://www.instagram.com/accounts/login/ajax/'
#    username = "SessionDeneme"
#    password = "'G7&z-E/*Gx4k^"
#    session_vals = {}
#
#    def login(self):
#        _time: int = int(datetime.now().timestamp())
#
#        # get tokens from site
#        response: Response = requests.get(self.url)
#        # cookies = response.cookies
#        # cookie_jar = cookies.get_dict()
#        # return cookie_jar
#        # return response.text
#        csrf = response.cookies["csrftoken"]
#        payload = {
#            "username": self.username,
#            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{_time}:{self.password}",
#            "queryParams": {},
#            "optIntoOneTap": "false",
#        }
#
#        login_header = {
#            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)"
#            " Chrome/77.0.3865.120 Safari/537.36",
#            "X-Requested-With": "XMLHttpRequest",
#            "Referer": "https://www.instagram.com/accounts/login/",
#            "x-csrftoken": csrf,
#        }
#
#        login_response: Response = requests.post(
#            self.login_url, data=payload, headers=login_header
#        )
#
#        json_data = json.loads(login_response.content)
#        cookies = login_response.cookies
#        cookie_jar = cookies.get_dict()
#
#        self.session = {
#            "csrf_token": cookie_jar["csrftoken"],
#            "session_id": cookie_jar["sessionid"],
#        }
#        return self.session
#
#        raise Exception(login_response.text)
