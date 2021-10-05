from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import imgshow as ig


def preprocess(img):
    '''
    Does preprocessing to the Images, to extract major features.
    Includes Gaussian, histogram based thresholding to obtain binary image. 
    Morphological transforms to remove noise. 
    Canny edge detection to get edges. 
    Returns an image with edges. 
    '''

    blur = cv2.GaussianBlur(img,(5,5),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    counts, bins, bars = plt.hist(gray.ravel(),256,[0,256])
    #plt.show()
    shape = img.shape
    print(shape)

    sum = 0
    divisor = 0
    for i in range(256):
        sum += (256-i)*(counts[i])
        divisor += counts[i]

    cutoff = (sum/divisor) + 40
    print(cutoff)

    #equ = cv2.equalizeHist(gray)
    #cv2.imshow('res.png',equ)
    #plt.hist(equ.ravel(),256,[0,256]);
    #plt.show()

    #ret,bin = cv2.threshold(gray,cutoff,255,cv2.THRESH_BINARY_INV)

    ret,bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ig.show_inv("OTSU", bin)

    kernel_1 = np.ones((5,5),np.uint8)
    kernel_2 = np.ones((3,3), np.uint8)
    skel = cv2.erode(bin, kernel_2, iterations = 1)
    skel_2 = cv2.erode(skel, kernel_2, iterations = 1)
    #dil = cv2.dilate(skel,kernel_2, iterations = 1)
    ig.show_inv('eroded', skel_2)

    edge = cv2.Canny(skel_2, 100,200)

    return skel_2
