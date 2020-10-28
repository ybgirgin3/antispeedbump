import os, sys
from PIL import Image

# resmin width'ini bul
# sonra onu width / height ile çarp

img = Image.open('mavili uzun resim.jpg')
w,h = img.size

new_width = 600
new_height = int(new_width * float(h) / float(w))

img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('resized.jpg')


"""
size = 128, 128

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)
"""
