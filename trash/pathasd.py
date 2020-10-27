import ntpath

def path_leaf(path):
  #path, filename = ntpath.split(path)
  with open(path, 'r') as f:
    x = f.read().splitlines()
    f.close()
  return x



print(path_leaf('/home/berkay/code/INSTAGRAM/antispeedbump/text_files/like_tag_file.txt'))
