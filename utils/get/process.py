from typing import Optional
import requests

from .expressions import Expressions
from utils.fp import FileProcess

HEADERS = FileProcess("headers", root="configs/settings").read()


class Process:
    "Fetching and Parsing Control Center"

    def __init__(self, username: Optional[str] = "",
                 custom_headers: Optional[dict] = {},
                 content: Optional[dict] = {}
                 ):
        # vars
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        self.headers = self._complete_dict(custom_headers)
        self.content = content

    def _complete_dict(self, custom_headers):
        tmp = HEADERS
        tmp.update(custom_headers)
        return tmp

    def fetch(self):
        resp = requests.get(url=self.url, headers=self.headers)
        return resp.json()

    def parse(self):
        return Expressions(data=self.content).parse()
