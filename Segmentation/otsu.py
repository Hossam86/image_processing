# Original paper :--> N. Otsu. A threshold selection method from gray level histograms. IEEE Transactions on Systems, Man and Cybernetics,9(1):62{66, 1979.
# Implementing Otsu segmentation from scratch python
# otsu method
# works best if the histogram of the image is bi-modal, but can be applied to other histograms as well

# using skiage lib 

import cv2
import numpy as np
from PIL import Image
from skimage.filters.thresholding import threshold_otsu

# read original image
original_image = Image.open("Segmentation/Data/sem3.png")

# spinwheel image has shadwow on the wheel so the wheeel not segmented right
# original_image = Image.open("Segmentation/Data/spinwheel.png")

# convert to gray scale
gray_image = original_image.convert('L')

# convert it to nmmpy array foramt
gray_image = np.asarray(gray_image)

#  apply otsu theshilding
threshold = threshold_otsu(gray_image)

# threshold the image
segmented_image = gray_image*(gray_image > threshold)

# saving the image
cv2.imwrite("Segmentation/Data/otsu_output.png", segmented_image)
# cv2.imwrite("Segmentation/Data/otsu_output_spinwheel.png", segmented_image)

