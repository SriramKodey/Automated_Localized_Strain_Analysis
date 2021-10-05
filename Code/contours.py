import numpy as np
from cv2 import cv2
import imgshow as ig

def maxcontours(img):
    '''
    Returns an image with the maximum area square separated.
    Input has to be an edges images (Output of Canny),
    Output is a binary Image
    '''
    shape = img.shape
    shape = [shape[0], shape[1], 3]

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    fin = np.zeros(shape, dtype = np.uint8)

    maxArea = 0
    for i in range(int(len(contours))):
        temp = cv2.contourArea(contours[i])
        if(temp > maxArea):
            maxArea = temp

    n = len(contours)
    avgArea = 0
    for i in  range(int(n)):
        area = cv2.contourArea(contours[i])
        avgArea += area
    avgArea = int(avgArea/n)
    print(avgArea)

    for i in range(int(n)):
        area = cv2.contourArea(contours[i])
        if(int(area) > (avgArea/2)):
            fin = cv2.drawContours(fin, contours, i, (0,0,255), 3)
        else:
           continue

    fin_2 = np.zeros(shape, dtype = np.uint8)
    for i in range(int(n)):
        area = cv2.contourArea(contours[i])
        if(area == maxArea):
            fin_2 = cv2.drawContours(fin_2, contours, i, (0,255,0), 1)

    fin_blur = cv2.GaussianBlur(fin_2, (5,5), 0)

    ig.show_inv_color("contours", fin)
    ig.show_inv_color("maxArea", fin_2)
    ig.show_inv_color('Gaussian', fin_blur)

    h_input = cv2.cvtColor(fin_blur, cv2.COLOR_BGR2GRAY)
    ret,h_in = cv2.threshold(h_input,20,255,cv2.THRESH_BINARY)

    return h_in

if __name__ == "__main__":
    img = cv2.imread("C://Users/kodey/Documents/Python Scripts/DIC/Images//test8.jpg")
    maxcontours(img)