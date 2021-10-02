from os import read

import cv2
import numpy as np
from pydicom import dcmread
from matplotlib import pyplot as plt


def gray_scale_opencv():

    # read images
    img=cv2.imread("data\green-tree-leaf.jpg")

    # convert RGB image which is three channel ndarray to grayscale , which is an signle channel ndarray using 
    # y = 0:299 * R + 0:587 * G + 0:114 * B
    img_gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # write images
    cv2.imwrite('green-tree-leaf.jpg',img_gray_scale)


def gray_scale_pillow():
    from PIL import Image

    # Reading image 
    img=Image.open("data\green-tree-leaf.jpg")
    # converting it into grayscale.
    img_gray_scale=img.convert('L')
    # convert PIL Image object to numpy array
    img_gray_scale=np.array(img_gray_scale);
    # Converting ndarray to image for saving using PIL.
    im3 = Image.fromarray(img_gray_scale)


def gray_scale():
    import matplotlib.image as mpimg

    img = mpimg.imread('data\green-tree-leaf.jpg')
    # Convert an Image to Grayscale in Python Using the Conversion Formula and the matplotlib Library
    R,G,B= img[:,:,0],img[:,:,1],img[:,:,2]
    img_gray_scale = 0.299 * R + 0.587 * G + 0.114 * B

    plt.imshow(img_gray_scale,cmap='gray')
    plt.show()

def read_dicom():
    ds=dcmread("data/3DSlice260.dcm")
    # plot the image using matplotlib
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()

if __name__=='__main__':
    # gray_scale()
    read_dicom()
