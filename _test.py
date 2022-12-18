from utils import Parse, FileProcess



username = 'bellathorne'
content = FileProcess(filename=username).read()
ret = Parse(content=content).find_val()
