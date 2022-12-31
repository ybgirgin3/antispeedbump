from typing import Optional
import pathlib
import json
import os


class FileProcess:
    def __init__(self, filename: Optional[str], *args, **kwargs) -> None:
        # create root dir if not exists
        self.root_dir = kwargs.get("root", "sites")
        pathlib.Path(self.root_dir).mkdir(parents=True, exist_ok=True)

        self.filepath = os.path.join(self.root_dir, f'{filename}.json')
        self.content = kwargs.get('content', {})

    def __len__(self) -> dict:
        ret = dict()
        items = os.listdir(self.root_dir)
        ret[self.root_dir] = {
            "len": len(items),
            "items": items
        }
        return ret

    def read(self) -> dict:
        "read json"
        with open(self.filepath, "r") as f:
            ret = json.load(f)

        return ret

    def write(self) -> None:
        "write json files"
        print("filename in write: ")
        c2r = json.dumps(self.content, indent=2)
        with open(self.filepath, "w") as f:
            f.write(c2r)

    def is_site_exists(self) -> bool:
        "control if file exists"
        return pathlib.Path(self.filepath).is_file()
