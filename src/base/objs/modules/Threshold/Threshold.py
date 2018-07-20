import cv2
import numpy as np
from src.base.objs.Showable.Showable import Showable

class Threshold(Showable):

    INSTANCE_COUNT = 0

    # Values
    DEFAULT_MIN = 127
    DEFAULT_MAX = 255
    BLOCK_SIZE  = (3, 3)
    CONSTANT    = 0

    # Threshold Types
    BINARY      = cv2.THRESH_BINARY
    BINARY_INV  = cv2.THRESH_BINARY_INV
    TRUNC       = cv2.THRESH_TRUNC
    TO_ZERO     = cv2.THRESH_TOZERO
    TO_ZERO_INV = cv2.THRESH_TOZERO_INV

    # Adaptive Methods
    OTSU = cv2.THRESH_OTSU
    ADAPTIVE_MEAN     = cv2.ADAPTIVE_THRESH_MEAN_C
    ADAPTIVE_GAUSSIAN = cv2.ADAPTIVE_THRESH_GAUSSIAN_C


    def __init__(self):
        self.result = np.zeros((500, 500))
        self.min    = Threshold.DEFAULT_MIN
        self.max    = Threshold.DEFAULT_MAX
        self.type   = Threshold.BINARY
        self.method = Threshold.ADAPTIVE_MEAN
        self.blockSize = Threshold.BLOCK_SIZE
        self.constant  = Threshold.CONSTANT


        Threshold.INSTANCE_COUNT += 1

    def otsu(self, image):
        _, self.result = cv2.threshold(image, 0, 255, Threshold.BINARY | Threshold.OTSU)
        return self.result

    def threshold(self, image):
        _, self.result = cv2.threshold(image, self.min, self.max, self.type)
        return self.result

    def threshold2(self, image, min=DEFAULT_MIN, max=DEFAULT_MAX, type=BINARY):
        _, self.result = cv2.threshold(image, min, max, type)
        return self.result

    #FIX THE HARD CODED BLOCK SIZE
    def adaptiveThreshold(self, image):
        self.result = cv2.adaptiveThreshold(image, self.max, self.method, self.type, 13, self.constant)
        return self.result

    def adaptiveThreshold2(self, image, max, method, type, blockSize, constant):
        self.result = cv2.adaptiveThreshold(image, max, method, type, blockSize, constant)
        return self.result

    def __del__(self):
        Threshold.INSTANCE_COUNT -= 1

