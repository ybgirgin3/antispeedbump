
def compatible_aspect_ratio(size):
    min_ratio, max_ratio = 4.0 / 5.0, 90.0 / 47.0
    width, height = size
    ratio = width * 1.0 / height * 1.0
    print("FOUND: w:{w} h:{h} r:{r}".format(w=width, h=height, r=ratio))
    return min_ratio <= ratio <= max_ratio


