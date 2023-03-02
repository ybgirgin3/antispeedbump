import datetime
import json
from typing import Optional, Union

import requests
from antispeedbump.commons.models.schemas import Sites, Queue
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func


class DBProcess:
    def __init__(
        self,
        sess: Session,
        username: Optional[str],
    ) -> None:
        self.session = sess
        self.username = username

    def __len__(self):  # -> Union[int, float]:
        q = "select count(*) from sites"
        count = self.session.execute(q)
        return count

    def read(
        self,
        model: Union[Sites, Queue],
        column: str = "extracted_data",
        fetch_by: Optional[Union[tuple, str]] = "",
        # delete_perm: str = "n",
    ) -> dict:
        """
        Read data from table(s)
        """

        column_attr = getattr(model, column)
        ret = {}

        if isinstance(fetch_by, tuple):
            sub_q = getattr(model, fetch_by[0])
            resp = self.session.query(column_attr).where(
                sub_q == fetch_by[1]).first()
            ret = json.loads(resp[column])

        if isinstance(fetch_by, str):
            resp = self.session.query(model).order_by(func.random()).first()
            ret["id"] = resp.id
            ret["description"] = resp.description
            ret["binary_data"] = resp.binary_data
            ret["media"] = json.loads(resp.medias)
        return ret

    def write(self, content, extracted_content) -> None:
        """write json files"""

        # ** write sites db
        if extracted_content["is_private"] and "medias" not in extracted_content:
            return

        last_update = datetime.datetime.today()

        sites = Sites(
            username=self.username,
            data=json.dumps(content, indent=2),
            extracted_data=json.dumps(extracted_content, indent=2),
            last_update=last_update,
        )
        print("writing sites...")
        self.session.add(sites)
        self.session.commit()

        # ** write queue db
        mapped = [
            {
                "medias": json.dumps(m, indent=2),
                "description": emoji_validator(m['original_description'], self.username),
                "last_update": last_update,
                "binary_data": create_bin(m["download_url"]),
                "sites": self.username
            }
            for m in extracted_content["medias"]
        ]
        print("writing mapped queue")

        self.session.bulk_insert_mappings(Queue, mapped)
        self.session.commit()

    def update(self, content, extracted_content) -> None:
        """update json files"""
        updated_sites = Sites(
            data=json.dumps(content, indent=2),
            extracted_data=json.dumps(extracted_content, indent=2),
            last_update=datetime.datetime.today(),
        )
        self.session.add(updated_sites)
        self.session.commit()

    def delete(self, model: Union[Sites, Queue], data_id: int = 1) -> bool:
        _del = self.session.query(model).where(model.id == data_id).first()
        print("_Del: ", _del)
        self.session.delete(_del)
        self.session.commit()
        return True

    def is_site_exists(self) -> bool:
        """control if file exists"""
        return bool(
            self.session.query(Sites).where(
                Sites.username == self.username).first()
        )

    def is_site_still_valid(
        self,
        model: Sites,
    ) -> bool:
        """
        validation control
        if file last_update date is older than 10 days
        re-fetch data

        """
        # TODO: re-fetch olayını 10 gün de bir değil aynı zamanda medialar bittiğinde de tekrarla
        d = (
            self.session.query(model.last_update)
            .where(model.username == self.username)
            .first()
        )
        d = dict(d)
        return (
            True if (datetime.datetime.today() -
                     d["last_update"]).days <= 3 else False
        )


def create_bin(url: str):
    print("current url in create_bin: ", url)
    return requests.get(url).content


def complete_dict(raw_headers: dict = None, **kwargs):
    #  defaults
    for key in kwargs:
        val = kwargs.get(key, "")
        raw_headers.update(val)

    return raw_headers


def get_image_size(imp: str) -> tuple:
    """image must be exists

    Args:
        imp (str): image path

    Returns:
        tuple: (w,h)
    """

    from PIL import Image

    im = Image.open(imp)
    return im, im.size


def emoji_validator(original_description: str, username: str) -> str:
    # conversion = {
    #    "🤤": "&#129296;",
    #    #"🤤": "U0001F924",
    #    #"🤯": u'\uF92F',
    #    #"💀": "U+1F480",
    #    #"😳": "U+1F633",
    #    #"😩": "U+1F629",
    #    #"💥": "U+1F4A5",
    # }
    # + u'\u2764'

    # TODO: original_description içinde eğer sayfanın kendi adını "follow bla bla"
    # olarak tanıttığı bir kısım varsa onu regex ile ortadan kaldırmak lazım
    return f"""{remove_self_promotion(remove_emojis(original_description), username)}
    .......
    Follow for more content ✨❤️ 
    credit: @{username}

    #car
    #sportcar
    #{username}
    #luxurycar
    """


def remove_emojis(string: str) -> str:
    """
    remove emojis from desc
    4 char long emojis not supported in chromedriver
    """

    import emoji
    import random

    replacing_emojis = {
        "🎥": ["by", "camera", "cameraman"]
    }

    for char in string:
        if emoji.is_emoji(char):
            if char in replacing_emojis:
                rep = random.choice(replacing_emojis[char])
            else:
                rep = ""

            string = string.replace(char, rep)

    return string


def remove_self_promotion(string: str, username) -> str:
    """
    remove self promotion in original_description
    because I already promoting :)
    """
    string = string.split()
    for each in string:
        if each.startswith('@') and each == f"@{username}":
            string.remove(each)

    return " ".join(string)
