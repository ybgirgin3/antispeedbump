from .fp import FileProcess
import requests
import json
import os

HEADERS = json.load(open("configs/headers.json"))


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

    def __init__(self, filename: str) -> None:
        self.content = FileProcess(
            filepath=os.path.join('sites', filename)).read()
        print(self.content)
