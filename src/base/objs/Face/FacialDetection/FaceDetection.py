import cv2

from src.base.overlay.shapes.Rectangle import Rectangle


class FaceDetection:

    def __init__(self):
        self.cascadePath  = "../../assets/cascades/haarcascade_frontalface_default.xml"
        self.faceCascade  = cv2.CascadeClassifier(self.cascadePath)
        self.scaleFactor  = 1.25
        self.minNeighbors = 5
        self.minSize = (15, 15)

    def detect(self, frame):

        faces = self.faceCascade.detectMultiScale(
            frame,
            scaleFactor  = self.scaleFactor,
            minNeighbors = self.minNeighbors,
            minSize = self.minSize
        )

        faceROIs = []
        for (x, y, w, h) in faces:
            faceROIs.append(Rectangle(x, y, w, h))

        return faceROIs


    def getMinSize(self):
        return self.minSize

    def setMinSize(self, size):
        self.minSize = size

    def getScaleFactor(self):
        return self.scaleFactor

    def setScaleFactor(self, scaleFactor):
        self.scaleFactor = scaleFactor

    def getCascadePath(self):
        return self.cascadePath

    def setCascadePath(self, path):
        self.cascadePath = "../../assets/cascades/haarcascade_frontalface_default.xml"
