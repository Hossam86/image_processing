import cv2
from PIL import Image
import numpy as np

#  opening the image
# original_image = Image.open("Segmentation/Data/adaptive_example1.png")
original_image = Image.open("Segmentation/Data/spinwheel.png")

# Convert to gray scale
gray_image = original_image.convert('L')

# Convert to numpy array
gray_image = np.asarray(gray_image)

# Performing adaptive thresholding.
segmented_image = cv2.adaptiveThreshold(gray_image, gray_image.max(),
                                         cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

# Saving the image
# cv2.imwrite("Segmentation/Data/adaptive_output.png",segmented_image)
cv2.imwrite("Segmentation/Data/adaptive_output_spinwheel.png", segmented_image)
