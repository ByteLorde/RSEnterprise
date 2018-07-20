import wx
from PIL import Image
import cv2
import numpy as np

def GenerateEmptyImage(width, height):
    return np.zeros( (width, height, 3), np.uint8 )