import re
import os
import imutils
import numpy as np
import cv2
from RSEnterprise.src.base.overlay.point.Point import Point


class Template:

    @staticmethod
    def fromPath(path, label=""):
        assert os.path.exists(path), "ERROR: Can't create Template from non-existent file: " + os.path.abspath(path)
        # File name regular expression.
        regex = r'(.*/)?(.*).png'
        match = re.match(regex, path, re.I)
        name = match.groups()[-1]

        if not label:
            label = name

        image = cv2.imread(path)
        return Template(image, label, path)

    @staticmethod
    def fromImage(image, label=""):
        assert image is not None, "ERROR: Can't load template from blank image. : " + label
        return Template(image, label)

    def __init__(self, image=None, label="", path=""):
        self.image = image
        self.label = label
        self.path  = path

    def match(self, other, thresh=0.75, multiscale=True):
        return TemplateMatcher.matchTemplate(self, other, thresh, multiscale)

    def contains(self, other, thresh=0.75, multiscale=True):
        return len( self.match(other, thresh, multiscale) ) > 0

    def load(self, path):
        self.path = path
        self.image = cv2.imread(path)
        assert self.image != None, "Image cannot be loaded: " + path

    def getImage(self):
        return self.image.copy()

    def grayscale(self):
        if len( self.image.shape ) > 2:
            return cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2GRAY)
        return self.image.copy()

    def getAbsolutePath(self):
        return os.path.abspath(self.path)

    def getTemplateName(self):

        if not self.path:
            return ""

        # File name regular expression.
        regex = r'(.*/)?(.*).png'
        match = re.match(regex, self.path,  re.I)
        filename = match.groups()[-1]
        return filename if filename else self.path

    def getTemplatePath(self):
        # File path regular expression.
        regex = r'(.*/)?(.*).png'
        match = re.match(regex, self.path, re.I)
        filepath = match.groups()[0]
        return filepath if filepath else self.path

class TemplateMatcher:

    @staticmethod
    def matchTemplate(source, target, threshold=0.8, multiscale=True):

        sourceImage = source.grayscale()
        targetImage = target.grayscale()

        sourceCanny = cv2.Canny(sourceImage, 50, 200)
        targetCanny = cv2.Canny(targetImage, 50, 200)

        (sourceHeight, sourceWidth) = sourceCanny.shape[:2]
        (targetHeight, targetWidth) = targetCanny.shape[:2]

        cv2.imshow("Source", sourceImage)
        cv2.imshow("Target", targetImage)

        positives = []

        if multiscale:
            for scale in np.linspace(0.2, 1.0, 20)[::-1]:

                resizedImage = imutils.resize(targetImage, width=int(targetWidth * scale))
                (resizedHeight, resizedWidth) = resizedImage.shape[:2]

                r = targetWidth / float(resizedWidth)

                if resizedHeight < targetHeight or resizedWidth < targetWidth:
                    break

                resizedTemplate = Template(resizedImage, "")
                matches  = TemplateMatcher.matchTemplate(source, resizedTemplate, multiscale=False)

                # We must scale the endpoint by the r value for points found doing multiscale matching
                for match in matches:
                    startpoint = match[0]
                    endpoint   = match[1]
                    startpoint.x *= r
                    startpoint.y *= r
                    endpoint.x   *= r
                    endpoint.y   *= r
                    positives += ( startpoint, endpoint )

        result = cv2.matchTemplate(sourceCanny, targetCanny, cv2.TM_CCOEFF)

        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal < threshold:
            return positives

        (startX, startY) = (int(maxLoc[0]), int(maxLoc[1]))
        (endX,   endY)   = (int((maxLoc[0] + targetWidth)), int((maxLoc[1] + targetHeight)))

        startPoint = Point(startX, startY)
        endPoint   = Point(endX, endY)

        points = ( startPoint, endPoint )
        positives.append(points)

        return positives

    @staticmethod
    def findTemplate(templates, template, threshold=.75, multiscale=False):
        matches = []
        for item in templates:
            result = TemplateMatcher.matchTemplate(item, template, threshold, multiscale)
            if result:
                matches.append( ( item, result ) )
        return matches

