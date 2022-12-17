from typing import Optional


def write(filename: Optional[str], content: str) -> None:
    "write content to target file"
    with open(filename, content) as f:
        f.write(content)
