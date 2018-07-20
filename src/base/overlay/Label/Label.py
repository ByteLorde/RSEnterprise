import cv2

from src.base.objs.Color.Color import Color
from src.base.overlay.Component.Component import Component

class Label(Component):

    HERSHEY_SIMPLEX = 0
    HERSHEY_PLAIN   = 1
    HERSHEY_DUPLEX  = 2
    HERSHEY_COMPLEX = 3
    HERSHEY_TRIPLEX = 4
    HERSHEY_COMPLEX_SMALL  = 5
    HERSHEY_SCRIPT_SIMPLEX = 6
    HERSHEY_SCRIPT_COMPLEX = 7

    FONT_ITALIC = 16

    def __init__(self, text, color=Color.GREEN, style=HERSHEY_SIMPLEX, scale=1, thickness=1):
        super(Label, self).__init__(label="Label")
        self.text = text
        self.color = color
        self.style = style
        self.scale = scale
        self.thickness = thickness

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text

    def getTextSize(self):
        return cv2.getTextSize(self.text, self.style, self.scale, self.thickness)

    def drawComponent(self, image):
        x = self.x
        y = self.y
        if self.parent:
            x += self.parent.getAbsoluteX()
            y += self.parent.getAbsoluteY()
        cv2.putText(image, self.text, (x, y), self.style, self.scale, self.color, self.thickness)
        
    def getThickness(self):
        return self.thickness
    
    def setThickness(self, thickness):
        self.thickness = thickness

    def getScale(self):
        return self.scale

    def setScale(self, scale):
        self.scale = scale

    def getStyle(self):
        return self.style

    def setStyle(self, style):
        self.style = style

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
