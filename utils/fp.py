from typing import Optional, Union
import json
import yaml
import os


class FileProcess:
    def __init__(self, filename: str,
                 # content: Optional[Union[str, dict]],
                 dtype: str = "json",
                 *args, **kwargs
                 ) -> None:
        self.filepath = os.path.join('sites', f'{filename}.json')
        self.content = kwargs.get('content', {})
        self.dtype = dtype

    def read(self):
        "read json and yaml file"
        ret = None
        if self.dtype == "yml":
            ret = yaml.safe_load(open(self.filepath))
        else:
            with open(self.filepath, "r") as f:
                ret = json.load(f)

        return ret

    def write(self):
        "write json files"
        print("filename in write")
        c2r = ""
        if self.dtype == "json":
            c2r = json.dumps(self.content, indent=2)
        else:
            c2r = self.content

        with open(self.filepath, "w") as f:
            f.write(c2r)

    def is_site_exists(self) -> Union[str, None]:
        if os.path.exists(self.filepath):
            return self.filepath
        else:
            return None
