from utils import FileProcess, Fetch, Parse
import sys

# get data
username = sys.argv[1]

# if file exists
content = None
is_exists = FileProcess(filename=username).is_site_exists()
print("is_exists", is_exists)
if isinstance(is_exists, str):
    content = is_exists

# fetch data
elif not is_exists:
    resp = Fetch(username=username).fetch()
    saved_resp = FileProcess(filename=username, content=resp).write()

# extract content
content = FileProcess(filename=username).read()
extracted = Parse(content)
