from typing import Optional
import requests

from .expressions import Expressions
from utils.fp import FileProcess

HEADERS = FileProcess("headers", root="configs/settings").read()


def requester(url, *args, **kwargs):
    "request process"
    resp = requests.get(url=url, headers=kwargs.get('headers'))
    return resp


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
        resp = requester(self.url, headers=self.headers)
        return resp.json()

    def parse(self):
        return Expressions(data=self.content).parse()

    def create_content(self):
        media = self.content['media']
        download_url = media['download_url']
        code = media['code']
        resp = requester(url=download_url, stream=True)

        ret = {
            "path": f'/Users/berkay/Documents/workspace/Data/antispeedbump/posts/{code}.mp4',
            "description": "American Bull"
        }

        with open(ret['path'], "wb") as f:
            f.write(resp.content)

        return ret
