import cv2

from src.base.objs.Frame.Frame import Frame
from src.base.overlay.shapes.Rectangle import Rectangle


class CascadeObject:

    CASCADES_PATH = "/home/syndicate/PycharmProjects/Iris/assets/cascades/"

    FACE_FRONTAL_ALT     = "haarcascade_frontalface_alt.xml"
    FACE_FRONTAL_DEFAULT = "haarcascade_frontalface_default.xml"

    EYE           = "haarcascade_eye.xml"
    EYEPAIR_BIG   = "haarcascade_mcs_eyepair_big.xml"
    EYEPAIR_SMALL = "haarcascade_mcs_eyepair_small.xml"
    MOUTH         = "haarcascade_mcs_mouth.xml"
    NOSE          = "haarcascade_mcs_nose.xml"
    FACE_PROFILE  = "haarcascade_profileface.xml"
    PALM          = "palm.xml"
    FIST          = "fist.xml"

    SCALE_FACTOR  = 1.1
    MIN_NEIGHBORS = 3
    MIN_SIZE      = (15, 15)

    def __init__(self, type, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE):
        self.results      = None
        self.type         = type
        self.scaleFactor  = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize      = minSize
        self.loadCascade()

    def detect(self, image):
        self.image  = image

        self.results = self.cascade.detectMultiScale(
            self.image,
            scaleFactor =self.scaleFactor,
            minNeighbors=self.minNeighbors,
            minSize     =self.minSize
        )

        return self.results

    def resultsAsROI(self):
            resultsROI = []
            for (x, y, w, h) in self.results:
                ROI = Rectangle(x, y, w, h)
                resultsROI.append(ROI)
            return resultsROI

    def showResults(self):

            print("Showing")
            imageFrame     = Frame(self.image)
            iterationCount = 0

            for (x, y, w, h) in self.results:

                ROIRect    = Rectangle(x, y, w, h)
                ROI        = imageFrame.grabROI(ROIRect)
                frameTitle = "Cascade Result [" + str(iterationCount) + "]"
                subframe   = Frame(ROI, name=frameTitle)
                subframe.show()
                iterationCount += 1

    def loadCascade(self):
        cascade = CascadeObject.CASCADES_PATH + self.type
        self.cascade = cv2.CascadeClassifier(cascade)

    def default(self):
        self.results      = None
        self.scaleFactor  = CascadeObject.SCALE_FACTOR
        self.minNeighbors = CascadeObject.MIN_NEIGHBORS
        self.minSize      = CascadeObject.MIN_SIZE
        self.loadCascade()

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type
        self.loadCascade()

    def getScaleFactor(self):
        return self.scaleFactor

    def setScaleFactor(self, scaleFactor):
        self.scaleFactor = scaleFactor

    def getMinNeighbors(self):
        return self.minNeighbors

    def setMinNeighbors(self, minNeighbors):
        self.minNeighbors = minNeighbors

    def getMinSize(self):
        return self.minSize

    def setMinSize(self, minSize):
        self.minSize = minSize