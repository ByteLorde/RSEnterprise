import numpy as np
import cv2

class CannyEdgeDetection():

    INSTANCE_COUNT    = 0

    DEFAULT_SIGMA     = 0.33
    DEFAULT_TIGHT_MIN = 225
    DEFAULT_TIGHT_MAX = 250
    DEFAULT_WIDE_MIN  = 10
    DEFAULT_WIDE_MAX  = 200

    def __init__(self, sigma=DEFAULT_SIGMA):

        self.result   = None
        self.sigma    = sigma
        self.tightMin = CannyEdgeDetection.DEFAULT_TIGHT_MIN
        self.tightMax = CannyEdgeDetection.DEFAULT_TIGHT_MAX
        self.wideMin  = CannyEdgeDetection.DEFAULT_WIDE_MIN
        self.wideMax  = CannyEdgeDetection.DEFAULT_WIDE_MAX
        CannyEdgeDetection.INSTANCE_COUNT += 1


    def canny(self, image, min, max, edges=None, apertureSize=None, L2gradient=None):
        self.result = cv2.Canny(image, min, max, edges, apertureSize, L2gradient)
        return self.result

    def auto(self, image):

        v = np.median(image)

        lower = int(max(0, (1.0 - self.sigma) * v))
        upper = int(min(255, (1.0 + self.sigma) * v))

        self.result = cv2.Canny(image, lower, upper)

        return self.result

    def show(self):
        if self.result:
            cv2.imshow("Canny: " + str(CannyEdgeDetection.INSTANCE_COUNT), self.result)

    def default(self):
        self.result   = None
        self.sigma    = CannyEdgeDetection.DEFAULT_SIGMA
        self.tightMin = CannyEdgeDetection.DEFAULT_TIGHT_MIN
        self.tightMax = CannyEdgeDetection.DEFAULT_TIGHT_MAX
        self.wideMin  = CannyEdgeDetection.DEFAULT_WIDE_MIN
        self.wideMax  = CannyEdgeDetection.DEFAULT_WIDE_MAX

    def wide(self, image):
        self.result = cv2.Canny(image, self.wideMin, self.wideMax)
        return self.result

    def tight(self, image):
        self.result = cv2.Canny(image, self.tightMin, self.tightMax)
        return self.result

    def getTightMin(self):
        return self.tightMin

    def getTightMax(self):
        return self.tightMax

    def setTightMin(self, value):
        self.tightMin = value

    def setTightMax(self, value):
        self.tightMax = value

    def getWideMin(self):
        return self.wideMin

    def getWideMax(self):
        return self.wideMax

    def setWideMin(self, value):
        self.wideMin = value

    def setWideMax(self, value):
        self.wideMax = value

    def getSigma(self):
        return self.sigma

    def setSigma(self, sigma):
        self.sigma = sigma

    def __del__(self):
        CannyEdgeDetection.INSTANCE_COUNT -= 1



