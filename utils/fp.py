from typing import Optional, Union
import json
import yaml
import os


class FileProcess:
    def __init__(self, filename: str,
                 *args, **kwargs
                 ) -> None:
        self.filepath = os.path.join(
            kwargs.get("root", "sites"), f'{filename}.json')
        self.content = kwargs.get('content', {})

    def read(self):
        "read json"
        with open(self.filepath, "r") as f:
            ret = json.load(f)

        return ret

    def write(self):
        "write json files"
        print("filename in write")
        c2r = json.dumps(self.content, indent=2)
        with open(self.filepath, "w") as f:
            f.write(c2r)

    def is_site_exists(self) -> Union[str, None]:
        if os.path.exists(self.filepath):
            return self.filepath
        else:
            return None
