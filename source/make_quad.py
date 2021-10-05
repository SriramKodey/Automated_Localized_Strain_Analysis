import numpy as np
import math
from operator import itemgetter

lines = np.array([[ 544.2,          1.1309733],
                  [-117.166664,     2.172935 ],
                  [ 200.4,          2.1676989],
                  [ 230.33333,      1.1170107]])

def sort(lines):
    new_lines = sorted(lines, key=itemgetter(1))
    return new_lines


def solve(l1, l2):
    A = [[l1[0], l1[1]], [l2[0], l2[1]]]
    
    b = [l1[2], l2[2]]

    point = np.linalg.solve(A, b)

    return point

def get_corners(linesf):
    lines = sort(linesf)
    theta = np.array([lines[0][1], lines[1][1], lines[2][1], lines[3][1]])
    #print(theta)

    phi = np.array([lines[0][0], lines[1][0], lines[2][0], lines[3][0]])
    #print(phi)


    line_eqs = np.zeros((4,3))
    for i in range(4):
        line_eqs[i][0] = math.cos(theta[i])
        line_eqs[i][1] = math.sin(theta[i])
        line_eqs[i][2] = phi[i]

    #print(line_eqs)

    points =  np.zeros((4,2))

    points[0] = solve(line_eqs[0], line_eqs[2])
    points[1] = solve(line_eqs[0], line_eqs[3])
    points[2] = solve(line_eqs[1], line_eqs[3])
    points[3] = solve(line_eqs[1], line_eqs[2])

    #print(points)
    return points

if __name__ == "__main__":
    print(get_corners(lines))