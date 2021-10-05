import numpy as np
import math

class ellipse_var:
    def __init__(self, phi, X0_in, Y0_in, long_axis, short_axis):
        self.phi = phi
        self.X0_in = X0_in
        self.Y0_in = Y0_in
        self.long_axis = long_axis
        self.short_axis = short_axis


def fit_ellipse(x, y, axis_handle):
    orientation_tolerance = 1e-3

    x = x.T
    y = y.T

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    x = x - mean_x
    y = y - mean_y

    X = np.concatenate((np.square(x), np.multiply(x,y), np.square(y), x, y), axis=1)

    denom = np.linalg.inv((X.T)*X)

    arr = np.sum(X, axis = 0) * denom
    arr = np.array(arr)

    a = arr[0][0]
    b = arr[0][1]
    c = arr[0][2]
    d = arr[0][3]
    e = arr[0][4]

    if ( min( abs(b/a), abs(a/b) ) > orientation_tolerance) == True :
        orientation_rad = 0.5 * math.atan(b/(c-a))
        cos_phi = math.cos( orientation_rad )
        sin_phi = math.sin( orientation_rad )
        A = (a * cos_phi**2) - (b * cos_phi * sin_phi) + (c * sin_phi**2)
        B = 0
        C = (a * (sin_phi**2)) + (b * cos_phi * sin_phi) + (c * cos_phi**2)
        D = (d * cos_phi) - (e * sin_phi)
        E = (d * sin_phi) + (e * cos_phi)

        [mean_X, mean_Y] = [(cos_phi*mean_x - sin_phi*mean_y), (sin_phi*mean_x + cos_phi*mean_y)]

        print(orientation_rad)
    
    else:
        orientation_rad = 0
        cos_phi = math.cos(orientation_rad)
        sin_phi = math.sin(orientation_rad)
        A = a
        B = b
        C = c
        D = d
        E = e
        mean_X = mean_x
        mean_Y = mean_y

    test = A*C

    if(test > 0):
        status = ''
    
    elif test == 0:
        status = 'Parabola Found'
        print("fit_ellipse: Did not find an ellipse")
    
    else:
        status = 'Hyperbola Found'
        print("fit_ellipse: Did not find an ellipse")

    
    if(test > 0):
        if(A<0):
            A = -1*A
            C = -1*C
            D = -1*D
            E = -1*E

        X0 = mean_X - D/2/A
        Y0 = mean_Y - E/2/C
        F = 1 + (D**2)/(4*A) + (E**2)/(4*C)
        [A, B] = [(math.sqrt(F/A)),(math.sqrt(F/C))]

        long_axis = 2*max(A, B)
        short_axis = 2*min(A, B)

        R = np.array([[cos_phi, sin_phi], [-1*sin_phi, cos_phi]])
        P_in = np.dot(R,[[X0], [Y0]])
        X0_in = P_in[0]
        Y0_in = P_in[1]

        ell = ellipse_var(orientation_rad, X0_in, Y0_in, long_axis, short_axis)

        print(long_axis)
        print(short_axis)

        return ell
