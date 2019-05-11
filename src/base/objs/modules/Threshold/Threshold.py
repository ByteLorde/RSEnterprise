import cv2
import numpy as np
import os

from src.plugins.Bot.objs.template.Template import Template


class Threshold:
    INSTANCE_COUNT = 0

    # Values
    DEFAULT_MIN = 127
    DEFAULT_MAX = 255
    DEFAULT_COLOR = 255
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
    ADAPTIVE_CONSTANT = 13
    ADAPTIVE_BLOCK_SIZE  = 3


    def __init__(self):
        self.result = np.zeros((500, 500))
        self.min    = Threshold.DEFAULT_MIN
        self.max    = Threshold.DEFAULT_MAX
        self.type   = Threshold.BINARY
        self.method = Threshold.ADAPTIVE_MEAN
        self.constant  = Threshold.CONSTANT


        Threshold.INSTANCE_COUNT += 1

    """
    This method is an adaptive thresholding techinque that calculates the min threshold value based on the histogram
    of an image. The 0 passed in for the minvalue is arbitrary because it gets overriden with the OTSU flag. 
    """
    @staticmethod
    def otsu(template, type=BINARY):
        calculated_min, result = cv2.threshold(template.grayscale().getImage(), 0, 255, type | Threshold.OTSU)
        return result

    """
    Threshold takes a minimum pixel value (min) and sets every pixel >= min to the MAX value.
    
    TYPES:
        BINARY     - Sets all pixels < min to 0, all pixels > min to 255
        BINARY_INV - Sets all pixels < min to 255, all pixels > min to 0
        TRUNC      - Sets all pixels > min to 255, leaves all pixels < min as what they are.
        TOZERO     - Sets all pixels < min to 0, leaves all pixels > min as what they are. 
        TOZERO_INV - Sets all pixels > min to 0, leaves all pixels < min as what they are. 
    # Additional Documentation: https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
    """
    @staticmethod
    def threshold(template, min=DEFAULT_MIN, max=DEFAULT_MAX, type=BINARY):
        _, result = cv2.threshold(template.grayscale().getImage(), min, max, type)
        return result


    """
    Adaptive Thresholding doing use a set min value for thresholding.
    Instead, this method adapts that min value by regions in the image 
    To make for dynamic thresholding in an image that may have various lighting conditions
    
    Methods:
        ADAPTIVE_MEAN     - Threshold value is the mean of the neighboring area.
        ADAPTIVE_GAUSSIAN - Threshold value is the weighted sum of neighboring values, with weights as a Gaussian window.
    """
    @staticmethod
    def adaptiveThreshold(template, color=DEFAULT_COLOR, method=ADAPTIVE_MEAN, type=BINARY, blocksize=ADAPTIVE_BLOCK_SIZE, constant=ADAPTIVE_CONSTANT):
        r = cv2.adaptiveThreshold(template.grayscale().getImage(), color, method, type, blocksize, constant)

        return r
    #
    # def adaptiveThreshold2(self, image, max, method, type, blockSize, constant):
    #     self.result = cv2.adaptiveThreshold(image, max, method, type, blockSize, constant)
    #     return self.result

    def __del__(self):
        Threshold.INSTANCE_COUNT -= 1

if __name__ == "__main__":

    path = "book.png"

    type = "Threshold Type"
    adaptive_method = "Adaptive Method"
    min_val = "Min Value"
    target_color = "Target Color"

    cv2.namedWindow("Testing")
    window = "Testing"


    def nothing(x):
        pass


    cv2.createTrackbar(type, window, 0, 4, nothing)
    cv2.createTrackbar(adaptive_method, window, 0, 1, nothing)
    cv2.createTrackbar(min_val, window, 0, 255, nothing)
    cv2.createTrackbar(target_color, window, 0, 255, nothing)

    thresh_types = [
        Threshold.BINARY,
        Threshold.BINARY_INV,
        Threshold.TRUNC,
        Threshold.TO_ZERO,
        Threshold.TO_ZERO_INV
    ]

    thresh_methods = [
        Threshold.ADAPTIVE_MEAN,
        Threshold.ADAPTIVE_GAUSSIAN
    ]

    # cap = cv2.VideoCapture(0)

    while True:

        test_type = thresh_types[ cv2.getTrackbarPos(type, window) ]
        test_method = thresh_methods[ cv2.getTrackbarPos(adaptive_method, window) ]
        test_min = cv2.getTrackbarPos(min_val, window)
        test_color = cv2.getTrackbarPos(target_color, window)

        # ret, frame = cap.read()
        #
        # print(frame)
        #
        # testTemplate = Template.fromImage(frame, "Cam")
        testTemplate = Template.fromPath("book.png")
        normal_thresh = Threshold.threshold(testTemplate, test_min, test_color, test_type)
        adaptive_thresh = Threshold.adaptiveThreshold(testTemplate, test_color, test_method, test_type)
        otsu_thesh = Threshold.otsu(testTemplate, test_type)
        cv2.imshow("Normal", normal_thresh)
        cv2.imshow("Adaptive", adaptive_thresh)
        cv2.imshow("Otsu", otsu_thesh)
        k = cv2.waitKey(5)
        if k == ord('q'):
            break