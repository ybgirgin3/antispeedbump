from utils import headers
import requests


class Fetch:
    def __init__(self, username: str, custom_headers: dict = {}) -> None:
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        self.headers = self._complete_dict(custom_headers)

    def fetch(self):
        resp = requests.get(url=self.url, headers=self.headers)
        return resp.json()

    def _complete_dict(self, custom_headers):
        tmp = (headers.headers())
        tmp.update(custom_headers)
        return tmp
