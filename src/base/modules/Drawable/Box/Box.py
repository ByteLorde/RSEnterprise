from src.base.modules.Drawable.Drawable import Drawable
from src.base.modules.Drawable.point.Point import Point


class Box(Drawable):

    def __init__(self, width, height, x=0, y=0):
        super(Box, self).__init__(self)
        self.x = x
        self.y = y
        self.width  = width
        self.height = height

    def origin(self):
        return self.x, self.y

    def midpoint(self):
        x = self.width  // 2
        y = self.height // 2
        return Point(x, y)

    def getX(self):
        return self.x

    def setX(self, xCoord):
        self.x = xCoord

    def getY(self):
        return self.y

    def setY(self, yCoord):
        self.y = yCoord

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

