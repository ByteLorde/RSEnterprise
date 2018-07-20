import cv2

from src.base.objs.Color.Color import Color


class Drawable:

    ABOVE = 0
    BELOW = 1
    LEFT  = 2
    RIGHT = 3

    HERSHEY_SIMPLEX = 0
    HERSHEY_PLAIN   = 1
    HERSHEY_DUPLEX  = 2
    HERSHEY_COMPLEX = 3
    HERSHEY_TRIPLEX = 4
    HERSHEY_COMPLEX_SMALL  = 5
    HERSHEY_SCRIPT_SIMPLEX = 6
    HERSHEY_SCRIPT_COMPLEX = 7

    FONT_ITALIC = 16

    def __init__(self):
        self.color = Color.GREEN

    def putText(self, image, text, ROI, type=ABOVE, font=HERSHEY_TRIPLEX, scale=1, color=Color.GREEN, thickness=1,
                xOffset=0, yOffset=0):

        origins = {
                    Drawable.ABOVE: ( ROI.x, ROI.y - 10 ),
                    Drawable.BELOW: ( ROI.x, ROI.relativeHeight + 10 ),
                    Drawable.LEFT : ( ROI.x - 2 * len(text), ROI.y),
                    Drawable.RIGHT: ( ROI.relativeWidth + 10, ROI.y)
                  }

        originX = origins[type][0] + xOffset
        originY = origins[type][1] + yOffset
        cv2.putText(image, text, (originX, originY), font, scale, color, thickness)

    def drawRect(self, image, ROI, thickness=1):
        cv2.rectangle(image, ROI.origin(), ROI.relativeSize(), self.color, thickness)

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
