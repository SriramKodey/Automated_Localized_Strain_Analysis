import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2
from cluster import dbscan
import imgshow as ig
from cluster import kmeans

def hough_method(edge):
    lines = cv2.HoughLines(edge,1,np.pi/180,100)
    n = int(lines.size/2)
    shape = edge.shape
    shape = [shape[0], shape[1], 3]
    disp = np.full(shape, 255, dtype = np.uint8)

    for i in range(n):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(disp,(x1,y1),(x2,y2),(0, 0, 255),2)

    ig.show("all lines", disp)

    return lines


# HoughP method
def houghp_method(edge):
    ig.show('edge',edge)

    lines = cv2.HoughLinesP(edge,1,np.pi/180,120,5)

    n = int(lines.size / 4)
    print(n)
    #print(lines)
    for i in range(n):
        x1 = lines[i][0][0]
        y1 = lines[i][0][1]
        x2 = lines[i][0][2]
        y2 = lines[i][0][3]

        #cv2.line(blur,(x1,y1),(x2,y2),(0,255,255),2)

    #cv2.line(test,(0,0),(200,200),(0,0,255),2)
    #show('image',blur)

    return lines

def drawlines(lines, img):
    n = int(lines.size/2)

    for i in range(n):
        rho = lines[i][0]
        theta = lines[i][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    ig.show('image',img)        
        
def extract_lines(img):
    '''
    Image, lines -- Returned. 
    Returns Image with the lines drawn and also the lines in an array.
    '''
    lines = hough_method(img)
    n = int((lines.size)/2)
    print(n)
    rho = np.zeros(n)
    theta = np.zeros(n)
    areas = np.zeros(n)
    colors = np.random.rand(n)

    for i in range(int(n)):
        rho[i] = ((lines[i][0][0])/100)
        theta[i] = lines[i][0][1]

        areas[i] = 2

    plt.clf()
    plt.scatter(rho, theta, s=areas, c=colors, alpha=0.5)
    plt.show()

    n = len(rho)

    X = np.zeros((n,2))

    for i in range(int(n)):
        X[i][0] = rho[i]
        X[i][1] = theta[i]


    clusters = np.zeros(n)
    clusters = kmeans(X)

    n_c = 4

    lines4 = np.zeros((n_c,4))

    for i in range(n):
        t = clusters[i]

        if t == -1:
            lines4[3][0] += rho[i]
            lines4[3][1] += 1

            lines4[3][2] += theta[i]
            lines4[3][3] += 1

        lines4[t][0] += rho[i]
        lines4[t][1] += 1

        lines4[t][2] += theta[i]
        lines4[t][3] += 1

    linesf = np.zeros((n_c, 2), dtype = np.float32)

    for i in range(n_c):
        linesf[i][0] = ((lines4[i][0]/lines4[i][1])*100)
        linesf[i][1] = (lines4[i][2]/lines4[i][3])


    shape = img.shape
    shape = [shape[0], shape[1], 3]
    disp = np.full(shape, 255, dtype = np.uint8)
    drawlines(linesf, disp)

    disp_g = cv2.cvtColor(disp, cv2.COLOR_BGR2GRAY)
    bin,thresh = cv2.threshold(disp_g, 20, 255, cv2.THRESH_BINARY_INV)

    return thresh, linesf