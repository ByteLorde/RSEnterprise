import cv2
import numpy as np

from src.base.objs.Color.Color import Color
from src.base.objs.Face.FacialDetection.FaceDetection import FaceDetection
from src.base.objs.ROI.ROI import ROI
from src.base.objs.Showable.Showable import Showable
from src.base.objs.Transformation.Transformations import Transformable
from src.base.objs.Drawable.Drawable import Drawable
from src.base.objs.modules.ContourDetection.ContourDetection import ContourDetection
from src.base.objs.modules.Threshold.Threshold import Threshold


class Frame(Transformable, Drawable, Showable):

    LEFT  = 0
    RIGHT = 1
    ABOVE = 2
    BELOW = 3

    faceDetector = FaceDetection()
    contourDetection = ContourDetection()
    thresholder = Threshold()

    def __init__(self, image, name="Image Frame"):
        Transformable.__init__(self, image)
        Drawable.__init__(self)
        Showable.__init__(self)
        self.result = image
        self.name = name

    def grabROI(self, rect):
        image = self.crop(self.result, rect)
        return ROI(image, self, rect)

    def detectFaces(self):
        return Frame.faceDetector.detect(self.result)

    def drawFaces(self):
        faceROIs = self.detectFaces()
        for ROI in faceROIs:
            self.drawRectangle(ROI)
        return faceROIs

    def getMask(self):
        return np.zeros(self.result.shape)

    def drawRectangle(self, ROI, thickness=1):
        super().drawRect(self.result, ROI, thickness)

    def findContours(self, mode=contourDetection.mode, method=contourDetection.method):
        return self.contourDetection.findContours(self.getWorkableCopy(), mode, method)

    def grayscale(self):
        return cv2.cvtColor(self.result.copy(), cv2.COLOR_BGR2GRAY)

    def adaptiveThreshold(self):
        return self.thresholder.adaptiveThreshold(self.getWorkableCopy())

    def threshold(self, min=thresholder.min, max=thresholder.max, type=thresholder.type):
        return self.thresholder.threshold2(self.result.copy(), min, max, type)

    def getWorkableCopy(self):
        grayscale = self.grayscale()
        threshold = self.thresholder.adaptiveThreshold(grayscale)
        return threshold

    def drawContours(self, heiarchyPosition=-1, color=(255, 0, 0), thickness=1):
        contours = self.findContours(Frame.contourDetection.mode, Frame.contourDetection.method)
        self.result = cv2.drawContours(self.result, contours, heiarchyPosition, color, thickness)
        return self.result

    def putText(self, text, ROI, type=ABOVE, font=Drawable.HERSHEY_TRIPLEX, scale=1, color=Color.GREEN, thickness=1,
                xOffset=0, yOffset=0):
        super().putText(self.result, text, ROI, type, font, scale, color, thickness, xOffset, yOffset)
