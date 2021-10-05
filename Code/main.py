import numpy as np
from loader import load
from preprocessing import preprocess
from imgshow import show
from contours import maxcontours
import lines
from transform import transform
from make_quad import get_corners
import cv2


def driver(img):
    edge = preprocess(img)

    max_cont_img = maxcontours(edge)

    lines_img, linesf = lines.extract_lines(max_cont_img)
    #show('lines', lines_img)

    lines.drawlines(linesf, img)

    new_corners =  get_corners(linesf)
    x = np.array([new_corners[0][0], new_corners[1][0], new_corners[2][0], new_corners[3][0]])
    y = np.array([new_corners[0][1], new_corners[1][1], new_corners[2][1], new_corners[3][1]])

    transform(x, y, img)

if __name__ == "__main__":
    #path = "C://Users/kodey/Documents/Python Scripts/DIC/Images//test8.jpg"
    img = load()
    driver(img)
    