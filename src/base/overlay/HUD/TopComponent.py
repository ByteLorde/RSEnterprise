from src.base.overlay.Crosshair.Crosshair import Crosshair
from src.base.overlay.Label.Label import Label
from src.base.overlay.TimeLabel import TimeLabel
from src.base.overlay.container.Container import Container
from src.base.overlay.point.Point import Point


class TopComponent(Container):

    def __init__(self):
        super().__init__(label="TopComponent")
        self.createDateTimeComponent()

    def createDateTimeComponent(self):
        timeLabel = TimeLabel()
        timeLabel.setX(100)
        timeLabel.setY(100)
        self.addChild(timeLabel)
        crosshair = Crosshair()
        crosshair.setSize(10)
        crosshair.setLocation(Point(150, 250))
        self.addChild(crosshair)

    def setFrame(self, frame):
        self.frame = frame
        self.width = frame.shape[0]
        self.height = frame.shape[1]
