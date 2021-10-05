from cv2 import cv2
import numpy as np
from tkinter import filedialog

def load():
    path = filedialog.askopenfilename()

    img = cv2.imread(path)

    return img