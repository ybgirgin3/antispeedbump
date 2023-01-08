from typing import Optional
import requests

from .expressions import Expressions
from ..utils import FileProcess, complete_dict

GET_HEADERS = FileProcess("get", root="configs/settings/get").read()


class Process:
    """Fetching and Parsing Control Center"""

    def __init__(self, username: Optional[str] = "",
                 custom_headers: Optional[dict] = {},
                 content: Optional[dict] = {},
                 post_index: int = 0,
                 shortcode: Optional[str] = ""
                 ):
        # vars
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        # tmp.update({"Referer": f"https://www.instagram.com/{self.username}/"})
        _custom_headers = {
            "referer": f"https://www.instagram.com/{self.username}/",
        }
        # update headers
        custom_headers.update(_custom_headers)
        self.headers = complete_dict(
            raw_headers=GET_HEADERS,
            custom_headers=custom_headers)

        self.content = content
        self.post_index = post_index
        self.shortcode = shortcode

    def fetch(self):
        # resp = requester(self.url, headers=self.headers)
        resp: requests.Response = requests.get(
            url=self.url, headers=self.headers)
        return resp
        # return resp.json()

    def parse(self) -> dict:
        return Expressions(data=self.content, post_index=self.post_index, shortcode=self.shortcode).parse()

    def create_content(self) -> dict:
        media = self.content['media']
        download_url = media['download_url']
        code = media['code']
        suffix = media['suffix']
        is_video = media['is_video']
        # resp = requester(url=download_url)
        resp: requests.Response = requests.get(url=download_url)

        ret = {
            "path": f'/Users/berkay/Documents/workspace/Data/antispeedbump/posts/{code}.{suffix}',
            "is_video": is_video}

        with open(ret['path'], "wb") as f:
            f.write(resp.content)

        return ret
