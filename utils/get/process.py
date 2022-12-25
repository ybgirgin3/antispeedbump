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
                 content: Optional[dict] = {},
                 post_index: int = 0
                 ):
        # vars
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        self.headers = self._complete_dict(custom_headers)
        self.content = content
        self.post_index = post_index

    def _complete_dict(self, custom_headers):
        tmp = HEADERS
        tmp.update({"Referer": f"https://www.instagram.com/{self.username}/"})
        tmp.update(custom_headers)
        return tmp

    def fetch(self):
        resp = requester(self.url, headers=self.headers)
        return resp.json()

    def parse(self):
        return Expressions(data=self.content, post_index=self.post_index).parse()

    def create_content(self):
        media = self.content['media']
        download_url = media['download_url']
        code = media['code']
        suffix = media['suffix']
        is_video = media['is_video']
        resp = requester(url=download_url, stream=True)

        ret = {
            "path": f'/Users/berkay/Documents/workspace/Data/antispeedbump/posts/{code}.{suffix}',
            "is_video": is_video}

        with open(ret['path'], "wb") as f:
            f.write(resp.content)

        return ret
