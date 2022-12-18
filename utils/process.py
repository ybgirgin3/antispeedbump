from .fp import FileProcess
from .expressions import Expressions
import requests
import json
import ast

HEADERS = FileProcess("headers", root="configs").read()
#CONTENT_PATHS = FileProcess("content_paths", root="configs").read()

class Fetch:
    "Create a request and get data from api"

    def __init__(self, username: str, custom_headers: dict = {}) -> None:
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        self.headers = self._complete_dict(custom_headers)

    def fetch(self):
        resp = requests.get(url=self.url, headers=self.headers)
        return resp.json()

    # inner utils
    def _complete_dict(self, custom_headers):
        tmp = HEADERS
        tmp.update(custom_headers)
        return tmp


class Parse:
    "Parse data which recieved from Fetch(line 6)"

    def __init__(self, content: str) -> None:
        self.content = content

    def find_val(self):
        return Expressions(data=self.content).parse()

