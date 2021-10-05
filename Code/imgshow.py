from cv2 import cv2
import numpy as np

def show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_inv(name, img):
    inv = cv2.bitwise_not(img)
    cv2.imshow(name, inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_inv_color(name, img):
    inv = cv2.bitwise_not(img)
    grey = cv2.cvtColor(inv, cv2.COLOR_BGR2GRAY)
    bin, thres = cv2.threshold(grey, 250, 255, cv2.THRESH_BINARY)
    cv2.imshow(name, thres)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   