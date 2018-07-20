import cv2
import numpy as np

from src.base.objs.Color.Color import Color
from src.base.overlay.HUD.TopComponent import TopComponent
from src.base.overlay.Label.Label import Label
from src.base.overlay.border.Border import Border
from src.base.overlay.line.Line import Line



class Overlay:

    def __init__(self, frame):

        self.frame = frame
        self.createOverlay()

    def createOverlay(self):

        self.mask = np.zeros(self.image.rows. self.image.cols)
        self.createBorder()

    def createBorder(self):

        lineSize = 100
        vertices = Border.getBoundingBox()

        for i in range(4):

            cornerPiece1 = Line(lineSize, 0,)

    def drawBorder(self):
        #border.draw(self.image)
        pass

    def draw(self):
        self.drawBorder()


tc = TopComponent()

while(1):
    img = np.zeros((1000, 1000, 3), np.uint8)


    tc.setFrame(img)
    tc.drawComponent(img)
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF


    if k == 27:
        break


cv2.destroyAllWindows()