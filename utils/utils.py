import datetime
import json
from typing import Optional, Union
import random

from commons.models.schemas import Sites, Queue
from sqlalchemy import insert
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
        delete_perm: str = "n",
    ) -> list[dict]:
        """
        Read data from table(s)
        """

        column_attr = getattr(model, column)
        print("column attr: ", column_attr)

        if isinstance(fetch_by, tuple):
            sub_q = getattr(model, fetch_by[0])
            resp = self.session.query(column_attr).where(sub_q == fetch_by[1]).first()
            ret = json.loads(resp[column])

        if isinstance(fetch_by, str):
            ret = {}
            resp = self.session.query(model).order_by(func.random()).first()
            ret["description"] = resp.description

            # ret = json.loads(resp[column])
            # NOTE: fix dynamic column name
            media = json.loads(resp.medias)
            ret["media"] = media

            if delete_perm.lower() in ("y", "yes"):
                self.delete(model, resp.id)

        return ret

    def write(self, content, extracted_content) -> None:
        """write json files"""

        # ** write sites db
        sites = [
            {
                "username": self.username,
                "data": json.dumps(content, indent=2),
                "extracted_data": json.dumps(extracted_content, indent=2),
                "last_update": datetime.datetime.today(),
            }
        ]
        self.session.execute(insert(Sites), sites)

        # ** write queue db
        mapped = [
            {
                "medias": json.dumps(m, indent=2),
                "description": emoji_validator(),
            }
            for m in extracted_content["medias"]
        ]

        self.session.bulk_insert_mappings(Queue, mapped)
        self.session.commit()

    def update(self, content, extracted_content) -> None:
        """update json files"""
        updated_data = {
            "data": json.dumps(content, indent=2),
            "extracted_data": json.dumps(extracted_content, indent=2),
            "last_update": datetime.datetime.today(),
        }

        self.session.query(Sites).update(updated_data)
        self.session.commit()

    def delete(self, model: Union[Sites, Queue], data_id: int = 1) -> None:
        _del = self.session.query(model).where(model.id == data_id).first()
        self.session.delete(_del)
        self.session.commit()

    def is_site_exists(self) -> bool:
        """control if file exists"""
        return bool(
            self.session.query(Sites).where(Sites.username == self.username).first()
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
            True if (datetime.datetime.today() - d["last_update"]).days <= 3 else False
        )


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


def emoji_validator() -> str:
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

    # return conversion[random.choice(list(conversion.keys()))]
    return "Follow for more content ✨"
