import cv2

from src.base.objs.Showable.Showable import Showable

"""
Design features:
Log every blurred image in a history, store a copy 
"""
class GaussianBlur(Showable):

    INSTANCE_COUNT  = 0

    DEFAULT_KSIZE  = (3, 3)
    DEFAULT_SIGMAX = 0
    DEFAULT_SIGMAY = None
    DEFAULT_BORDER = None

    def __init__(self, kSize=DEFAULT_KSIZE):

        self.result     = None
        self.kSize      = kSize
        self.sigmaX     = GaussianBlur.DEFAULT_SIGMAX
        self.sigmaY     = GaussianBlur.DEFAULT_SIGMAY
        self.borderType = GaussianBlur.DEFAULT_BORDER
        GaussianBlur.INSTANCE_COUNT += 1

    def blur(self, image):
        self.result = cv2.GaussianBlur(image, self.kSize, self.sigmaX)
        return self.result

    def default(self):
        self.result = None
        self.kSize = GaussianBlur.DEFAULT_KSIZE
        self.sigmaX = GaussianBlur.DEFAULT_SIGMAX
        self.sigmaY = GaussianBlur.DEFAULT_SIGMAY
        self.borderType = GaussianBlur.DEFAULT_BORDER

    def getkSize(self):
        return self.kSize

    def setKsize(self, kSize):
        self.kSize = kSize

    def getSigmaX(self):
        return self.sigmaX

    def setSigmaX(self, sigma):
        self.sigmaX = sigma

    def getSigmaY(self):
        return self.sigmaY

    def setSigmaY(self, sigma):
        self.sigmaY = sigma

    def getBorderType(self):
        return self.borderType

    def setBorderType(self, borderType):
        self.borderType = borderType

    def __del__(self):
        GaussianBlur.INSTANCE_COUNT -= 1