from datetime import datetime

from src.base.overlay.Label.Label import Label


class TimeLabel(Label):

    def __init__(self):
        super().__init__("", scale=.8)

    def drawComponent(self, image):
        self.setText( self.getTime() + str( self.getTextSize() ))
        super().drawComponent(image)

    def getTime(self):
        return str(datetime.now())