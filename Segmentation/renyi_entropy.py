import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import cumsum
import skimage.exposure as imexp
from numpy.lib.type_check import imag
from PIL import Image


def renyi_seg_fn(im, alpha):
    hist, hist_centers = imexp.histogram(im)
    #plot 
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].imshow(im, cmap=plt.cm.gray)
    axes[0].axis('off')
    axes[1].plot(hist_centers, hist, lw=2)
    axes[1].set_title('histogram of gray values')
    plt.show()

    # Convert all values to float
    hist_float = np.array([float(i) for i in hist])
    # Compute the pdf
    pdf = hist_float/np.sum(hist_float)
    # Compute the cdf
    cumsum_pdf = np.cumsum(pdf)
    s, e = im.min(), im.max()
    scalar = 1.0/(1-alpha)
    #  A very small value to prevent error due to
    eps = np.spacing(1)
    rr = e-s
    h1 = np.zeros((rr, 1))
    h2 = np.zeros((rr, 1))

    #  The following loop computes the  h1 nad h2
    #  values used to compute he entropy

    for ii in range(1, rr):
        iidash = ii+s
        temp0 = pdf[0:iidash]/cumsum_pdf[iidash]
        temp1 = np.power(temp0, alpha)
        h1[ii] = np.log(np.sum(temp1)+eps)

        temp0 = pdf[iidash+1:e]/(1.0-cumsum_pdf[iidash])
        temp2 = np.power(temp0, alpha)
        h2[ii] = np.log(np.sum(temp2) + eps)

    T = h1+h2
    # Entropy value is calculated
    T = T*scalar
    T = T.reshape((rr, 1))[:-2]
    # location where the maximum entropy
    # occurs is the threshold for the renyi entropy
    thresh = T.argmax(axis=0)

    return thresh


def renyi_seg_fn2(im, alpha):
    hist, _ = imexp.histogram(im)
    # Convert all values to float
    hist_float = np.array([float(i) for i in hist])
    # compute the pdf
    pdf = hist_float/np.sum(hist_float)
    # compute the cdf
    cumsum_pdf = np.cumsum(pdf)
    s, e = im.min(), im.max()
    scalar = 1.0/(1.0-alpha)
    # A very small value to prevent error due to log(0).
    eps = np.spacing(1)
    rr = e-s
    # The inner parentheses is needed because
    # the parameters are tuple.
    h1 = np.zeros((rr, 1))
    h2 = np.zeros((rr, 1))
    # The following loop computes h1 and h2
    # values used to compute the entropy.
    for ii in range(1, rr):
        iidash = ii+s
        temp0 = pdf[0:iidash]/(cumsum_pdf[iidash])
        temp1 = np.power(temp0, alpha)
        h1[ii] = np.log(np.sum(temp1)+eps)
        temp0 = pdf[iidash+1:e]/(1.0-cumsum_pdf[iidash])
        temp2 = np.power(temp0, alpha)
        h2[ii] = np.log(np.sum(temp2)+eps)
    T = h1+h2
    # Entropy value is calculated
    T = T*scalar
    T = T.reshape((rr, 1))[:-2]
    # location where the maximum entropy
    # occurs is the threshold for the renyi entropy
    thresh = T.argmax(axis=0)
    return thresh


# Read original image
original_image = Image.open("Segmentation/Data/CT.png")

# Convert to gray scale
gray_image = original_image.convert('L')

# Convert it to nmmpy array foramt
gray_image = np.asarray(gray_image)

# Computing the threshold by calling the function.
thresh = renyi_seg_fn(gray_image, 0.99)
print('The renyi threshold is: ', thresh[0])

# Threshold the image
segmented_image = 255*(gray_image > thresh)

# Saving the image
cv2.imwrite("Segmentation/Data/renyi_output.png", segmented_image)
