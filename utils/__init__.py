# get 
from .get import Process

# post
from .post import Post

# general
from .fp import FileProcess

import os
def _delete(item_p: dict):
    os.remove(item_p['path'])
    