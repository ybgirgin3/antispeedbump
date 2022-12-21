from utils import Process, FileProcess
from pprint import pprint



username = 'bellathorne'
content = FileProcess(filename=username).read()
ret = Process.Parse(content=content).find_val()
pprint(ret)


