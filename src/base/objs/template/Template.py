import re
import os
import numpy as np
import cv2

from src.base.objs.layer.Layer import Layer
from src.base.modules.Drawable.point.Point import Point

class Template:

    @staticmethod
    def fromPath(path, label=""):
        assert os.path.exists(path), "ERROR: Can't create Template from non-existent file: " + os.path.abspath(path)

        if not label:
            # File name regular expression.
            regex = r'(.*/)?(.*).png'
            match = re.match(regex, path, re.I)
            name = match.groups()[-1]

            label = name

        image = cv2.imread(path)
        return Template(image, label, path)

    @staticmethod
    def fromImage(image, label=""):
        assert image is not None, "ERROR: Can't load template from blank image. : " + label
        return Template(image, label)

    @staticmethod
    def copy(other):
        return Template(other.image, other.label, other.path)

    @staticmethod
    def blank(width, height):
        blankImage = np.zeros(width, height)
        return Template(blankImage)

    def __init__(self, image=None, label="", path=""):
        self.image   = image
        self.label   = label
        self.path    = path
        self.layers  = []

    def find(self, other, thresh=0.75, multiscale=False):
        return TemplateMatcher.matchTemplate(self, other, thresh, multiscale)

    def matchAll(self, other, thresh=0.75, multiscale=False):
        return TemplateMatcher.matchTemplate(self, other, thresh, multiscale)

    def contains(self, other, thresh=0.75, multiscale=False):
        return len( self.find(other, thresh, multiscale) ) > 0

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image

    def grayscale(self):

        if len( self.image.shape ) > 2:
            grayscaled = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.setImage(grayscaled)

        return self

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

    def show(self, title=""):
        assert self.image is not None, "Cannot show Template with no image!"

        if not title:
            title = self.label

        cv2.imshow(title, self.image)

        if cv2.waitKey(10000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(1)

    def draw(self):

        canvas = self.copy().getImage()

        for layer in self.layers:
            layer.draw(canvas)


        # for pointset in points:
        #     start = pointset[0]
        #     end   = pointset[1]
        #     cv2.rectangle(self.image, (start.x, start.y), (end.x, end.y), color, thickness)

    def getTemplatePath(self):
        # File path regular expression.
        regex = r'(.*/)?(.*).png'
        match = re.match(regex, self.path, re.I)
        filepath = match.groups()[0]
        return filepath if filepath else self.path

    def scale(self, percent):
        assert self.image is not None, "Cannot resize Template with no image!"

        width  = int( self.image.shape[1] * percent )
        height = int( self.image.shape[0] * percent )
        dims = (width, height)

        return cv2.resize(self.image, dims, interpolation=cv2.INTER_AREA)

    def resize(self, width=None, height=None):
        assert self.image is not None, "Cannot resize Template with no image!"

        width  = width  or self.getWidth()
        height = height or self.getHeight()
        dims = (width, height)

        return cv2.resize(self.image, dims, interpolation=cv2.INTER_AREA)

    def addLayer(self, layer):
        if not layer:
            return

        if not isinstance(layer, Layer):
            return

        self.layers.append(layer)

    def getLayers(self):
        return self.layers

    def resetLayers(self):
        self.layers = []

    def setLayers(self, layers):

        if not layers:
            return

        if not isinstance(layers, list):
            return

        self.layers = layers

    def getHeight(self):
        return self.image.shape[0]

    def setHeight(self, height):
        width = self.getWidth()
        dims = (width, height)
        return cv2.resize(self.image, dims, interpolation=cv2.INTER_AREA)

    def getWidth(self):
        return self.image.shape[1]

    def setWidth(self, width):
        height = self.getHeight()
        dims = (width, height)
        return cv2.resize(self.image, dims, interpolation=cv2.INTER_AREA)

class TemplateMatcher:

    @staticmethod
    def matchTemplate(source, target, threshold=0.8, multiscale=False):

        sourceImage = source.grayscale().getImage()
        targetImage = target.grayscale().getImage()
        w, h = target.getWidth(), target.getHeight()

        res = cv2.matchTemplate(sourceImage, targetImage, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        matches = []
        for pt in zip(*loc[::-1]):
            start = Point(pt[0], pt[1])
            end   = Point(pt[0] + w, pt[1] + h)
            matches.append((start, end))

        return matches

    @staticmethod
    def findTemplate(templates, template, threshold=.75, multiscale=False):
        matches = []
        for item in templates:
            result = TemplateMatcher.matchTemplate(item, template, threshold, multiscale)
            if result:
                matches.append( (item, result) )
        return matches

if __name__ == "__main__":
    template1 = Template.fromPath("./assets/inventory.png")
    # grayed = Template.fromImage(template1.grayscale())
    # grayed.show()

    template2 = Template.fromPath("./assets/leather.png")
    matches = template1.find(template2, thresh=.50)
    template1.draw()
    template1.show()

