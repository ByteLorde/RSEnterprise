from src.base.overlay.border.Border import Border

class Component:

    def __init__(self, label="Component"):
        self.x = 0
        self.y = 0
        self.width  = 0
        self.height = 0
        self.label  = label
        self.parent = None
        self.border = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def translateX(self, translation):
        self.x += translation

    def translateY(self, translation):
        self.y += translation

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getAbsoluteX(self):
        return self.x if not self.parent else self.x + self.parent.getAbsoluteX()

    def getAbsoluteY(self):
        return self.y if not self.parent else self.y + self.parent.getAbsoluteY()

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def removeParent(self):
        self.parent = None

    def update(self):
        self.x += self.parent.x
        self.y += self.parent.y

    def getBoundingBox(self):
        return ( self.x, self.y, self.width, self.height )

    def setBorder(self, border):
        self.border = border

    def drawComponent(self, image):
        pass