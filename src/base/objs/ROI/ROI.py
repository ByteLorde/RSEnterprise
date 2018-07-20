

"""
ROI - Region of Interest
"""
from src.base.overlay.shapes.Rectangle import Rectangle


class ROI(Rectangle):

    def __init__(self, image):
        super().__init__(ROI.x, ROI.y, ROI.relativeWidth, ROI.relativeHeight)
        self.result     = image
        self.superframe = superframe
        self.ROI = ROI

    def setBorder(self, newBorder):
        self.border = newBorder

    def draw(self):
        self.border.draw()

    def innerROI(self, rect):
        rect.setX(self.x + rect.x)
        rect.setY(self.y + rect.y)
        return rect

    def drawROI(self, thickness=1):
        self.draw()
        self.superframe.drawRect(self.ROI, thickness)

    def superframe(self):
        return self.superframe

