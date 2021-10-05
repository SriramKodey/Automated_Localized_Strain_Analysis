import numpy as np
from fit_ell import fit_ellipse
from fit_ell import ellipse_var
from cv2 import cv2
import math


x = [316, 17, 335, 637]
y = [454, 251, 91, 298]


def transform(x, y, img):
       xs = np.array([0, 1, 1, 0])
       ys = np.array([0, 0, 1, 1])
       As = np.array([[xs[0], xs[1], xs[2]], [ys[0], ys[1], ys[2]], [1, 1, 1]])
       Bs = np.array([[xs[3]], [ys[3]], [1]])

       S1 = np.linalg.solve(As, Bs)

       # each element is an array, so use Afs[0][0][0] to get the first element
       Afs = np.array([[S1[0][0]*xs[0], S1[1][0]*xs[1], S1[2][0]*xs[2]],
              [S1[0][0]*ys[0], S1[1][0]*ys[1], S1[2][0]*ys[2]],
              [S1[0][0], S1[1][0], S1[2][0]]])

       xp = [x[0], x[1], x[2], x[3]]
       yp = [y[0], y[1], y[2], y[3]]

       Ap = [[xp[0], xp[1], xp[2]], [yp[0], yp[1], yp[2]], [1, 1, 1]]
       Bp = [[xp[3]], [yp[3]], [1]]

       S2 = np.linalg.solve(Ap, Bp)

       Afp = np.array([[S2[0][0]*xp[0], S2[1][0]*xp[1], S2[2][0]*xp[2]],
              [S2[0][0]*yp[0], S2[1][0]*yp[1], S2[2][0]*yp[2]],
              [S2[0][0], S2[1][0], S2[2][0]]])

       Afs_inv = np.linalg.inv(Afs)

       T = np.mat(Afp) * np.mat(Afs_inv)

       circlex = [0.5, 1, 0.8535, 0.5, 0]
       circley = [0, 0.5, 0.8535, 1, 0.5]

       circle = np.matrix([circlex, circley, [1, 1, 1, 1, 1]])

       transformed_circle = T * circle

       transformed_circle = transformed_circle / transformed_circle[2][:]
       transformed_circle = np.round(transformed_circle)

       ellipse_points_x = transformed_circle[0]
       ellipse_points_y = transformed_circle[1]

       e = fit_ellipse(ellipse_points_x, ellipse_points_y,0)

       centre = (round(e.X0_in[0]), round(e.Y0_in[0]))
       axes = (round(e.long_axis/2), round(e.short_axis/2))

       cv2.ellipse(img, centre, axes, -((e.phi*180)/math.pi), 0, 360, (0,255,0), 2)

       cv2.imshow('ellipse', img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()


if __name__ == "__main__":
       img = cv2.imread("C://Users/kodey/Documents/Python Scripts/DIC/Images/test6.jpg")
       transform(x, y, img)


