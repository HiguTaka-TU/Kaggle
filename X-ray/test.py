import pydicom
import numpy as np
from pydicom.pixel_data_handlers.util import apply_voi_lut
import matplotlib.pyplot as plt
from PIL import Image

def dicom2array(path,voi_lut = True,fix_monochrome=True):
	dicom =pydicom.read_file(path)
	if voi_lut:
		data=apply_voi_lut(dicom.pixel_array,dicom)
	else:
		data=dicom.pixel_array

	if fix_monochrome and dicom.PhotometricInterpretation =="MONOCHROME1":
		data=np.amax(data)-data
	
	data = data-np.min(data)
	data = data/np.max(data)
	#data = (data*255).astype(np.uint8)
	
	return data

def resize(array,size,keep_ratio=False,resample=Image.LANCZOS):
	im=Image.fromarray(array)

	if keep_ratio:
		im.thumbnail((size,size),resmaple)
	else:
		im=im.resize((size,size),resample)

	return im


img = dicom2array('000434271f63a053c4128a0ba6352c7f.dicom')
im=resize(img,256)
im=np.array(im)
plt.figure(figsize=(2.56,2.56))
plt.imshow(im,'gray')
plt.savefig("1.png")
