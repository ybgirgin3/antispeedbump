import datetime
import json
from typing import Optional

from commons.models.schemas import Sites
from sqlalchemy import insert
from sqlalchemy.orm import Session


class DBProcess:
    def __init__(self,
                 sess: Session,
                 username: Optional[str],
                 ) -> None:
        self.session = sess
        self.username = username

    def __len__(self):  # -> Union[int, float]:
        q = "select count(*) from sites"
        count = self.session.execute(q)
        return count

    def read(self, column: str = 'extracted_data') -> list[dict]:
        """read json"""
        s = None
        if column == "data":
            s = Sites.data
        if column == 'extracted_data':
            s = Sites.extracted_data

        d = self.session.query(s).where(
            Sites.username == self.username
        ).first()
        return json.loads(d[0])

    def write(self, content, extracted_content) -> None:
        """write json files"""
        _d = [
            {
                'username': self.username,
                'data': json.dumps(content, indent=2),
                'extracted_data': json.dumps(extracted_content, indent=2),
                'last_update': datetime.datetime.today()
            }
        ]

        print("filename in write: ")
        self.session.execute(insert(Sites), _d)
        self.session.commit()

    def update(self, content, extracted_content) -> None:
        """update json files"""
        _d = {
            # 'username': self.username,
            'data': json.dumps(content, indent=2),
            'extracted_data': json.dumps(extracted_content, indent=2),
            'last_update': datetime.datetime.today()
        }

        self.session.query(Sites).update(
            _d
        )
        self.session.commit()


    def is_site_exists(self) -> bool:
        """control if file exists"""
        return bool(self.session.query(Sites).where(
            Sites.username == self.username
        ).first())

    def is_site_still_valid(self,
                            model: Sites,
                            ) -> bool:
        d = self.session.query(model.last_update).where(
            model.username == self.username
        ).first()
        d = dict(d)

        # datetime.datetime.strptime(d, "%Y-%m-%d")

        return True \
            if (datetime.datetime.today() - d['last_update']).days <= 2 \
            else False


# DB OLMADIGI ICIN SQL CALISMIYOR DB'YI ILK ETAP DA OLUSTURMAK LAZIM
#####

# util
# GET_HEADERS = FileProcess("get", root="configs/settings/get").read()


def complete_dict(raw_headers: dict = None,
                  **kwargs
                  ):
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
