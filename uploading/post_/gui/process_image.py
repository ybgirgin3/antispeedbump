from PIL import Image
import numpy as np
import scipy
import os

def correct_ratio(data):
	# will return true
	from instabot.api.api_photo import compatible_aspect_ratio, get_image_size
	return compatible_aspect_ratio(get_image_size(data))

def strip_exif(img):
	data = list(img.getdata())
	img_wout_exif = Image.new(img.mode, img.size)
	img_wout_exif.putdata(data)
	return img_wout_exif

def prep_and_fix(data):
	"""
		data must be path of the image
	"""
	with open(data, 'rb') as f:
		last_image_name = data.split('/')
		pic_name = os.path.splitext(last_image_name[-1])[0]
		img = Image.open(f)
		img = strip_exif(img)
		if not correct_ratio(data):
			img = crop_maximize_entropy(img)
		photo = os.path.join('araba_postları/sent_photos', '{}.jpg'.format(pic_name))
		img.save(photo)
	return photo


def _entropy(data):
	""" calculate the entropy of an image """
	hist = np.array(Image.fromarray(data).histogram())
	hist = hist / hist.sum()
	hist = hist[hist != 0]
	return -np.sum(hist * np.log2(hist))

def crop(x, y, data, w, h):
	x = int(x)
	y = int(y)
	return data[y : y + h, x : x + w]

def crop_maximize_entropy(img , min_ratio=4 / 5, max_ratio=90 / 47):
	from scipy.optimize import minimize_scalar

	w,h = img.size
	data = np.array(img)
	ratio = w / h

	if ratio > max_ratio:
		# çok geniş demektir
		w_max = int(max_ratio * h)


		def _crop(x):
			return crop(x, y=0, data=data, w=w_max, h=h)


		xy_max = w - w_max
	else:
		# çok dar
		h_max = int(w / min_ratio)

		def _crop(y):
			return crop(x=0, y=y, data=data, w=w, h=h_max)

		xy_max = h - h_max

	to_minimize = lambda xy: -_entropy(_crop(xy))
	x = minimize_scalar(to_minimize, bounds=(0, xy_max), method="bounded").x
	return Image.fromarray(_crop(x))

