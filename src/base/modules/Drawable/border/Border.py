import cv2

from src.base.modules.Drawable.line.Line import Line
import numpy as np

from src.base.modules.Drawable.point.Point import Point


class Border:

    NONE   = 0
    LINE   = 1
    DOTTED = 2
    DASHED = 3
    FRAMED = 4

    def __init__(self, borderType=LINE, thickness=50, color=(200,200,200)):
        self.borderType = borderType
        self.thickness  = thickness
        self.color      = color
        self.lines      = []

        self.createBorder()

    def createBorder(self):

        img = np.zeros((1000, 1000, 3), np.uint8)

        vertices = self.getBoundingBox()
        width  = self.width
        height = self.height
        lines  = []
        for i in range(len(vertices)):
            rotation  = i * 90
            rotation2 = (i + 1) * 90

            length = width if i % 2 == 0 else height
            if self.borderType == Border.FRAMED:
                length //= 4

            line  = Line(vertices[i % len(vertices)], angle=rotation,length=length, lineType=self.borderType, thickness=self.thickness, color=self.color)
            line2 = Line(vertices[i % len(vertices)], angle=rotation2,length=length, lineType=self.borderType, thickness=self.thickness, color=self.color)
            lines.append(line)
            lines.append(line2)

        lines = self.normalizeLineLengths(lines)
        for line in lines:
            line.draw(img)

        cv2.imshow("Tax", img)

    def normalizeLineLengths(self, lines):

        largestLength = 0

        for line in lines:
            largestLength = max(largestLength, line.length)

        for index in range(len(lines)):
            line = lines[index]
            line.setLength(largestLength)
            lines[index] = line

        return lines


    def createDashedBorder(self):

        img = np.zeros((1000, 1000, 3), np.uint8)
        vertices = self.getBoundingBox()

        width  = self.width
        height = self.height
        lines  = []

        for i in range(len(vertices)):
            rotation = 90 * i
            length = width if i % 2 == 0 else height
            line = Line(vertices[i], angle=rotation,length=length)
            cv2.putText(img, str(rotation), line.origin.origin(), 1, 5, self.color, self.thickness)
            lines.append(line)

        for line in lines:
            line.draw(img)
            cv2.line(img, line.origin.origin(), line.endPoint.origin(), (255,255, 0), 1, 8, 0)
        cv2.imshow("Oh", img)


    def getBoundingBox(self):
        vertex1 = Point(self.x, self.y)
        vertex2 = Point(self.relativeWidth, self.y)
        vertex3 = Point(self.relativeWidth, self.relativeHeight)
        vertex4 = Point(self.x, self.relativeHeight)

        vertices = (vertex1, vertex2, vertex3, vertex4)
        return vertices


    def draw(self, image):
        for line in self.lines:
            line.draw(image)

