---
marp: true
---

## Histogram based Segmentation 
In the histogram based method, a Threshold is determined by using the histogram of the image each pixel in image compared with threshold value. 
If the pixel intenisty is less than the threshold value, the corresponding pixel in the segemnted image is aasigned avlue of zero, If the pixel 
intensity is greater than the threshold value, the corrsponding pixel in the segmented image is assigned avalue of 1 Thus,

if pv is greater than or equal threshold then:
    segpv=1
else
    segpv=0

where pv is the pixel value in the image and segpv the pixel value in the segemnted image

histogram based methods use differnts technique  in determining the threshold, we Will discusss Ostsu's method and Renyi Entropy methods.
In images with anon uniform background a global threshold value from the histogram based mrthod might  be optimal

### Otsu's  Method [Ots79] 
works best if the histogram of the image is bi-modal but can be applied to other types histogram as well.
bimodal histogam is a type of histogram containg two peaks sperated by valley. one peak is the background and the other is the forground,

#### How
Otsu's algorithms search for threshold value that maxmimize the variance between the groups or minmize the vaiance within the group
(see Image Processing and acquisition using python page 169)

sample usage from scikit-image and also we will find its from scratch implmnetation in this repo. 

```python:
skimage.filter.threshold_ostsu(image, nbins=256) 
inputs:
image: input image in gray scale
nbins(optionl): number of bins that should be considered to calculate the histogram.
```

# Otsu's draw backs:
very dependant on image pixel values so it may not segment images with shadows well (see example of spin wheel in repo)



