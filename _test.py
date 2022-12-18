from utils import Parse, FileProcess
from utils import Expressions
from pprint import pprint



username = 'bellathorne'
content = FileProcess(filename=username).read()
ret = Parse(content=content).find_val()
pprint(ret)


