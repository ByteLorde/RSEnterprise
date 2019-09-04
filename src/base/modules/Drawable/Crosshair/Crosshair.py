from src.base.modules.Drawable.line.Line import Line
from src.base.modules.Drawable.point.Point import Point


class Crosshair:

    def __init__(self, size=5):
        self.midpoint = Point(0, 0)
        self.size = size
        self.thickness = 1
        self.line1 = Line(self.midpoint, thickness=self.thickness)
        self.line2 = Line(self.midpoint, thickness=self.thickness)
        self.adjustLines()

    def setSize(self, size):
        self.line1.setLength(size)
        self.line2.setLength(size)
        self.adjustLines()

    def setThickness(self, thickness):
        self.thickness = thickness

    def adjustLines(self):
        self.line1.setAngle(90)
        self.line1.translateY( -5 )
        # self.line2.translateX( int( -.5 * self.line2.length) )

    def setLocation(self, point):
        self.location = point
        self.line1.setOrigin(self.location)
        self.line2.setOrigin(self.location)
        self.adjustLines()

    def drawComponent(self, image):
        self.line1.draw(image)
        self.line2.draw(image)


