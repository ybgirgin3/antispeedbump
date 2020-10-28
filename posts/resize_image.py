import cv2
import argparse

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True)
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
print('old -> w: {}, h: {}'.format((image.shape[1]), (image.shape[0])))
image = image_resize(image, height=600)
print('new -> w: {}, h: {}'.format((image.shape[1]), (image.shape[0])))
cv2.imshow("image", image)
cv2.waitKey(0)
