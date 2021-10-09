from typing import Mapping
import cv2
import numpy as np
from numpy.lib.type_check import imag
from scipy import ndimage
import scipy

 
def mean_filter(img_gray_scale):
    """ Mean filter to image
    ===
    Advantages: 
    1. Remove noise
    2. Enhances the overall quality of the image, i.e., mean filter brightens an image."""

    # initializing the filter of size 5 by 5
    # The filter is divided by 25 for normalization
    k = np.ones((5, 5))/25

    # perfomaing convolution
    b = ndimage.filters.convolve(img_gray_scale, k)

    return b



def main():
    #  Open the image using cv2
    img = cv2.imread("data/ultrasound_muscle.png")
    # Converting the image to gray scale
    img_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply mean filter
    img_filter=mean_filter(img_gray_scale)
    # writing to file
    cv2.imwrite("data/mean_filter.png", img_filter)


if __name__=='__main__':
    main()