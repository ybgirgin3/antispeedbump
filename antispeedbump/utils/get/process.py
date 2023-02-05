import json
from typing import Optional

import requests

from .expressions import Expressions
from ..utils import complete_dict


def _(fn):
    with open(f"antispeedbump/configs/settings/get/{fn}") as f:
        return json.load(f)


GET_HEADERS = _("get.json")


class MediaProcess:
    """Fetching and Parsing Control Center"""

    def __init__(
        self,
        username: Optional[str] = "",
        custom_headers: Optional[dict] = {},
    ):
        # vars
        self.username = username
        self.url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
        # tmp.update({"Referer": f"https://www.instagram.com/{self.username}/"})
        _custom_headers = {
            "referer": f"https://www.instagram.com/{self.username}/",
        }
        # update headers
        custom_headers.update(_custom_headers)
        self.headers = complete_dict(
            raw_headers=GET_HEADERS, custom_headers=custom_headers
        )

    def fetch(self) -> dict:
        resp: requests.Response = requests.get(
            url=self.url, headers=self.headers)
        js = resp.json()
        return js

    def parse(
        self,
        content: Optional[dict] = {},
    ) -> dict:
        return Expressions(data=content).parse()
